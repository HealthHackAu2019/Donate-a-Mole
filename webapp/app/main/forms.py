from flask import url_for
from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import ValidationError
from wtforms.fields import (
    StringField,
    SubmitField,
    SelectField,
    HiddenField,
    BooleanField
)
from wtforms.validators import Email, EqualTo, InputRequired, Length, DataRequired, Email, URL, Optional

from app.models import Mole, User, Sex, Ancestry, History, NumNaevi

images = UploadSet('images', IMAGES)

class MoleForm(FlaskForm):
    sex = SelectField(
        'Sex',
        validators=[InputRequired()],
        choices=[(i, v) for i, v in enumerate(Sex.values)])

    age = StringField('Age', validators=[InputRequired()])

    ancestry = SelectField(
        'Ancestry',
        validators=[Optional()],
        choices=[(i, v) for i, v in enumerate(Ancestry.values)])
    
    body_location = HiddenField(validators=[InputRequired()])

    personal_history = SelectField(
        'Personal history of melanoma',
        validators=[Optional()],
        choices=[(i, v) for i, v in enumerate(History.values)])

    family_history = SelectField(
        'Family history of melanoma',
        validators=[Optional()],
        choices=[(i, v) for i, v in enumerate(History.values)])

    image = FileField(validators=[FileAllowed(images, 'Images only!')], render_kw={"accept": "image/*", "capture": "environment"})

    location = StringField("Postcode", validators=[Optional()])
    geo_long = HiddenField()
    geo_lat = HiddenField()

    contact_research = BooleanField(default=False)
    pathology = StringField('Pathology', validators=[Optional()])
    number_naevi = SelectField(
        'Number of moles',
        validators=[Optional()],
        choices=[(i, v) for i, v in enumerate(NumNaevi.values)])
    # image_path = db.Column(db.String(64))
    #recaptcha = RecaptchaField()

    submit = SubmitField('Submit')

    def validate(self):
      retValue = FlaskForm.validate(self)
      if not int(self.age):
          retValue = False
          self.age.errors.append("Not a number")
      if int(self.age) < 18:
          retValue = False
          self.age.errors.append("Not available for minors")
      return retValue