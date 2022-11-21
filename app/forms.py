from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , BooleanField
from wtforms.validators import DataRequired, EqualTo


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LogInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    #remember_me = BooleanField('Remember Me')
    submit = SubmitField()

class ReferralScreeningForm(FlaskForm):
    patient_name = StringField('Patient Full Name', validators=[DataRequired()])
    question1 = BooleanField('Does the Patient have a history of breast cancer at age ≤50')
    question2 = BooleanField('Does the Patient have a history of ovarian cancer at any age')
    question3 = BooleanField('Does the patients mother have a history of breast cancer at age ≤50')
    question4 = BooleanField('Does the patients mother have a history of ovarian cancer at any age')
    question5 = BooleanField('Does the patients sister have a history of breast cancer at age ≤50')
    question6 = BooleanField('Does the patients sister have a history of ovarian cancer at any age')
    question7 = BooleanField('Does the patients daughter have a history of breast cancer at age ≤50')
    question8 = BooleanField('Does the patients daughter have a history of ovarian cancer at any age')
    question9 = BooleanField('Does the patients maternal grandmother have a history of breast cancer at age ≤50')
    question10 = BooleanField('Does the patients maternal grandmother have a history of ovarian cancer at any age')
    question11 = BooleanField('Does the patients maternal aunt have a history of breast cancer at age ≤50')
    question12 = BooleanField('Does the patients maternal aunt have a history of ovarian cancer at any age')
    question13 = BooleanField('Does the patients paternal grandmother have a history of breast cancer at age ≤50')
    question14 = BooleanField('Does the patients paternal grandmother have a history of ovarian cancer at any age')
    question15= BooleanField('Does the patients paternal aunt have a history of breast cancer at age ≤50')
    question16= BooleanField('Does the patients paternal aunt have a history of ovarian cancer at any age')
    question17 = BooleanField('Does the Patient ≥ 2 cases of breast cancer after age 50 on same side of family')
    question18 = BooleanField('Does the Patient have a family history of male breast cancer')
    question19 = BooleanField('Is the patient of Jewish Ancestry')
    question20 = BooleanField('Does the patients mother have a history of ovarian cancer at any age')
    question21 = BooleanField('Does the Patient have a history of breast cancer at age 50')
    question22 = BooleanField('Does the Patient have a history of ovarian cancer at any age')
    question23 = BooleanField('Does the patients mother have a history of breast cancer at age ≤50')
    question24 = BooleanField('Does the patients mother have a history of ovarian cancer at any age')
    submit = SubmitField()

    

