from .. import db

class OAuth(db.model):
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(64), index=True)
    provider_user_id = db.Column(db.String(64), index=True)
    token = db.Column(db.String(64), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))