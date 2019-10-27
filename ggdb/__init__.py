from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '857284b3372527b303a344fd8cb890de'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gg.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from ggdb import routes