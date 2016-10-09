from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from wtforms import Form, StringField, PasswordField, validators
import bcrypt

app=Flask(__name__)

app.config['MONGO_DBNAME']='mongologinexample'
app.config['MONGO_URL']='mongodb://localhost:27017/mongologinexample'
mongo=PyMongo(app)

class userFom(Form):
    name=StringField('Name: ',validators=[Required()])
    email=StringField('Email Address', [validators.Email('Email')])
    password=PasswordField('New Password',[validators.DataRequired(),validators.EqualTo('cinfirm',message='Password must match')])
    confirm=Password('Repeat Password')

@app.route('/index')
def index():
	name=None
	form=user