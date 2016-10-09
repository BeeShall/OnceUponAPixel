from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from wtforms import Form, StringField, PasswordField, validators
import twilio.twiml
from twilio.rest import TwilioRestClient

from data.Model import Model

user_information={}



callers = {
    "+12018873871": "Santosh",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+14439852388": "Abhinav",
    "+12018878613": "Ashish Solta",
    "+13135798462": "Abish Solta",
    "+12017452101": "William"
}

app=Flask(__name__)

app.config['MONGO_DBNAME']='onceUponAPixel'
app.config['MONGO_URL']='mongodb://localhost:27017/onceUponAPixel'


mongo=PyMongo(app)

LIVE_FEEDS = []
@app.context_processor
def InjectFeed():
    return dict(LIVE_FEEDS=LIVE_FEEDS)

#@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
	if request.method=='POST':
		get_message()

	if 'username' in session:
		return render_template('lin_index.html',username=session['username'])
	return render_template('index.html')
	session.pop('san',None)

def get_message():
    number=request.form['From']
    from_number = request.values.get('From',None)
    image=request.form['MediaUrl0']

    global LIVE_FEEDS
    model = Model(image)
    tags = model.RunClarifai()
    story = model.GeneratePassage()

    LIVE_FEEDS = [[image, story]] + LIVE_FEEDS

    mongo.db.clarifai.insert({'number':str(from_number),'tags':tags,'image':image,'story':story})

    if from_number in callers:
    	message = ""
    else:
    	message = ""

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

@app.route('/login', methods=['POST'])
def login():
	session['username']='santosh'
	return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.route('/logout')
def logout():
	return render_template('index.html')



@app.route('/register', methods=['POST','GET'])
def register():
	return render_template('register.html')


@app.route('/echoData')
def echodata(methods=['GET', 'POST']):
    global LIVE_FEEDS
    return str(LIVE_FEEDS)

if __name__=='__main__':
	app.secret_key='mysecret'
	app.run(debug=True)