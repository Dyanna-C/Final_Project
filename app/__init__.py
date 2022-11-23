from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
# Create an instance of the Flask class - central object of the whole app
app = Flask(__name__)

# Add a SECRET_KEY to the app config
app.config['SECRET_KEY'] = 'you-will-never-guess'

# Configure the app using the Config class and the .from_object() method
app.config.from_object(Config)

# Create an instance of SQLAlchemy to represent our database
db = SQLAlchemy(app)

# Create an instance of Migrate to represent our migration engine
migrate = Migrate(app, db)
# Create an instance of LoginManager to let our app allow login capabilities
login = LoginManager(app)
login.login_view= 'login'
login.login_message_category = 'danger'

# import all of the routes from the routes module in the current folder
from . import routes, models

