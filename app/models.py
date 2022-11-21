from app import db
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin

class User(db.Model):
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