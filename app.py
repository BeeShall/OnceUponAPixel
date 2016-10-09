from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from wtforms import Form, StringField, PasswordField, validators
import bcrypt
import twilio.twiml
from twilio.rest import TwilioRestClient
import os


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

app.config['MONGO_DBNAME']='onceUponAPixel '
app.config['MONGO_URL']='mongodb://localhost:27017/onceUponAPixel '

app.config['TWILIO_SID']=os.environ.get('TWILIO_SID')
app.config['TWILIO_AUTH_TOKEN']=os.environ.get('TWILIO_AUTH_TOKEN')


mongo=PyMongo(app)

db_handle=mongo.db.clarifai

#@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
	if request.method=='POST':
		get_message()
		send_message(user_information['number'],user_information['name'])

	if 'username' in session:
		return render_template('lin_index.html',username=session['username'])
	return render_template('index.html')
	session.pop('san',None)

def get_message():
    number=request.form['From']
    from_number = request.values.get('From',None)
    image=request.form['MediaUrl0']
    image.save('/static/images')
    image_directory='/static/images'+str(image)
    db_handle.insert({'number':str(from_number),'tags':None,'image':'image_directory','story':None})
    if from_number in callers:
    	message = callers[from_number] + ", thanks for coming to //hackRamapo meeting"
    else:
    	message = "Hello there !, thanks for coming to //hackRamapo meeting!"
    resp = twilio.twiml.Response()
    resp.message(message)

    list_information.append(user_information)
    return str(resp)

def send_message(number,name):
	ACCOUNT_SID="AC0901e05ee44d2d33119019521dccda6f"
	AUTH_TOKEN="b52883f4ecee6325880ab3ffa0222c86"
	client=TwilioRestClient(ACCOUNT_SID,AUTH_TOKEN)
	client.messages.create(to=number,from_="+12016694967",
		body="Hey there ! Thanks for coming to //hackRamapo meeting")


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


	return ''

if __name__=='__main__':
	app.secret_key='mysecret'
	app.run(debug=True)