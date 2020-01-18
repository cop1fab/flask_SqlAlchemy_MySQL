from flask import  Flask
from flask_sqlalchemy import  SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(40), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(10))

def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = password

db.create_all()