from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_share import Share


app = Flask(__name__)
app.secret_key = 'my super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
share = Share(app)


from . import models, routes
