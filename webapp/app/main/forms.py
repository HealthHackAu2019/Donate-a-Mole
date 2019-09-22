from flask import url_for, current_app

from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import ValidationError
from wtforms.fields import (
    StringField,
    SubmitField,
    SelectField,
    HiddenField,
    BooleanField,
    IntegerField
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length, DataRequired, Email, URL, Optional

from app.models import Mole, User, Sex, Ancestry, History, NumNaevi
from app import imageSet

class MoleForm(FlaskForm):
    sex = SelectField(
        'Sex', coerce=int,
        validators=[InputRequired()],
        choices=[(i, v) for i, v in enumerate(Sex.values)])

    age = StringField('Age', validators=[InputRequired()])

    ancestry = SelectField(
        'Ancestry', coerce=int,
        validators=[Optional()],
        choices=[(i, v) for i, v in enumerate(Ancestry.values)])
    
    body_location = StringField(description="NONE", validators=[InputRequired()])
    body_image = StringField(description="NONE", validators=[InputRequired()])

    num_moles = IntegerField(description="NONE", default=1, validators=[InputRequired()])

    personal_history = SelectField(
        'Personal history of melanoma',
        validators=[Optional()], coerce=int,
        choices=[(i, v) for i, v in enumerate(History.values)])

    family_history = SelectField(
        'Family history of melanoma',
        validators=[Optional()], coerce=int,
        choices=[(i, v) for i, v in enumerate(History.values)])

    image = FileField(validators=[FileAllowed(imageSet, 'Images only!')], render_kw={"accept": "image/*", "capture": "environment"})

    
    geo_suburb = StringField("Suburb", validators=[Optional()])
    geo_state = StringField("State", validators=[Optional()])
    geo_long = StringField()
    geo_lat = StringField()

    contact_research = BooleanField(default=False)
    name = StringField("Name")
    dob = StringField("Date of Birth")
    email = EmailField("Email address", validators=[Optional(), Email()])

    pathology = StringField('Pathology', validators=[Optional()])
    number_naevi = SelectField(
        'Number of moles',
        validators=[Optional()], coerce=int,
        choices=[(i, v) for i, v in enumerate(NumNaevi.values)])

    submit = SubmitField('Submit')
