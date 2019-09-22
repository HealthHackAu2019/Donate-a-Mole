from flask import Blueprint, render_template, jsonify, current_app

from app.models import EditableHTML, Mole
from .forms import MoleForm
from app import db
from werkzeug.utils import secure_filename
import logging, string, random, os

logger = logging.getLogger("DaM")


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template(
        'main/about.html', editable_html_obj=editable_html_obj)

@main.route('/privacy')
def privacy():
    editable_html_obj = EditableHTML.get_editable_html('privacy')
    return render_template(
        'main/privacy.html', editable_html_obj=editable_html_obj)

def randStr(stringLength=10):
  letters = string.ascii_lowercase
  return ''.join(random.choice(letters) for i in range(stringLength))

@main.route('/donate', methods=["GET", "POST"])
def donate():
    form = MoleForm()
    if form.validate_on_submit():
        f = form.image.data
        filename = secure_filename(f.filename)
        logger.info(filename)
        filename = randStr(12) + filename
        fpath = os.path.join(current_app.instance_path, '../app/static/uploads/moles', filename)
        logger.info(filename)
        logger.info(fpath)
        f.save(fpath)
        mole = Mole()
        form.populate_obj(mole)
        mole.image_path=filename
        db.session.add(mole)
        db.session.commit()
        resp = jsonify(success=True)
        return resp
    return render_template(
        'main/donate.html', form=form)

    