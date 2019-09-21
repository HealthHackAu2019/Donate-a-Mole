from flask import Blueprint, render_template

from app.models import EditableHTML
from .forms import MoleForm

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

@main.route('/donate')
def donate():
    form = MoleForm()
    return render_template(
        'main/donate.html', form=form)