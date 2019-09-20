import flask
from flask import flash
from flask_security import current_user, login_user
from flask_dance.consumer import oauth_authorized
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_dance.contrib.google import make_google_blueprint
from sqlalchemy.orm.exc import NoResultFound
from myapp.models import db, OAuth, User


google_bp = make_google_blueprint(
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user)
)


# create/login local user on successful OAuth login
@oauth_authorized.connect_via(google_bp)
def github_logged_in(blueprint, token):
    if not token:
        flash("Failed to log in with GitHub.", category="error")
        return False

    resp = blueprint.session.get("/user")
    if not resp.ok:
        msg = "Failed to fetch user info from GitHub."
        flash(msg, category="error")
        return False

    github_info = resp.json()
    github_user_id = str(github_info["id"])

    # Find this OAuth token in the database, or create it
    query = OAuth.query.filter_by(
        provider=blueprint.name,
        provider_user_id=github_user_id,
    )
    try:
        oauth = query.one()
    except NoResultFound:
        oauth = OAuth(
            provider=blueprint.name,
            provider_user_id=github_user_id,
            token=token,
        )

    if oauth.user:
        # If this OAuth token already has an associated local account,
        # log in that local user account.
        # Note that if we just created this OAuth token, then it can't
        # have an associated local account yet.
        login_user(oauth.user)
        flash("Successfully signed in with GitHub.")

    else:
        # If this OAuth token doesn't have an associated local account,
        # create a new local user account for this user. We can log
        # in that account as well, while we're at it.
        user = User(
            # Remember that `email` can be None, if the user declines
            # to publish their email address on GitHub!
            email=github_info["email"],
            name=github_info["name"],
        )
        # Associate the new local user account with the OAuth token
        oauth.user = user
        # Save and commit our database models
        db.session.add_all([user, oauth])
        db.session.commit()
        # Log in the new local user account
        login_user(user)
        flash("Successfully signed in with GitHub.")

    # Since we're manually creating the OAuth model in the database,
    # we should return False so that Flask-Dance knows that
    # it doesn't have to do it. If we don't return False, the OAuth token
    # could be saved twice, or Flask-Dance could throw an error when
    # trying to incorrectly save it for us.
    return False