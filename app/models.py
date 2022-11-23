# from app import db
from flask_login import UserMixin
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash

# class User(db.Model):
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(256), nullable=False)

    # def __repr__(self):
    #     return '<User {}>'.format(self.username)    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set the password to the hashed version of the password
        self.password = self.set_password(kwargs.get('password', ''))
        # Add and commit the new instance to the database
        db.session.add(self)
        db.session.commit()

    def __str__(self):
        return self.username

    def set_password(self, plain_password):
        return generate_password_hash(plain_password)

    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#Add Model for referral form one to only one relationship with User
# class ReferralScreeningForm(FlaskForm):
class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)


#     question1 = BooleanField('Does the Patient have a history of breast cancer at age ≤50')
#     question2 = BooleanField('Does the Patient have a history of ovarian cancer at any age')
#     question3 = BooleanField('Does the patients mother have a history of breast cancer at age ≤50')
#     question4 = BooleanField('Does the patients mother have a history of ovarian cancer at any age')
#     question5 = BooleanField('Does the patients sister have a history of breast cancer at age ≤50')
#     question6 = BooleanField('Does the patients sister have a history of ovarian cancer at any age')
#     question7 = BooleanField('Does the patients daughter have a history of breast cancer at age ≤50')
#     question8 = BooleanField('Does the patients daughter have a history of ovarian cancer at any age')
#     question9 = BooleanField('Does the patients maternal grandmother have a history of breast cancer at age ≤50')
#     question10 = BooleanField('Does the patients maternal grandmother have a history of ovarian cancer at any age')
#     question11 = BooleanField('Does the patients maternal aunt have a history of breast cancer at age ≤50')
#     question12 = BooleanField('Does the patients maternal aunt have a history of ovarian cancer at any age')
#     question13 = BooleanField('Does the patients paternal grandmother have a history of breast cancer at age ≤50')
#     question14 = BooleanField('Does the patients paternal grandmother have a history of ovarian cancer at any age')
#     question15= BooleanField('Does the patients paternal aunt have a history of breast cancer at age ≤50')
#     question16= BooleanField('Does the patients paternal aunt have a history of ovarian cancer at any age')
#     question17 = BooleanField('Does the Patient ≥ 2 cases of breast cancer after age 50 on same side of family')
#     question18 = BooleanField('Does the Patient have a family history of male breast cancer')
#     question19 = BooleanField('Is the patient of Jewish Ancestry')
#     question20 = BooleanField('Does the patients mother have a history of ovarian cancer at any age')
#     question21 = BooleanField('Does the Patient have a history of breast cancer at age 50')
#     question22 = BooleanField('Does the Patient have a history of ovarian cancer at any age')
#     question23 = BooleanField('Does the patients mother have a history of breast cancer at age ≤50')
#     question24 = BooleanField('Does the patients mother have a history of ovarian cancer at any age')
#     submit = SubmitField()