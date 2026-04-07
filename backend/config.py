from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask (__name__) #init flask app
CORS(app) #disable CORS error 

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db" #what type of db and which file (where)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) #create instance of db