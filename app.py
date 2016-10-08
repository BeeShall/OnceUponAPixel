import os
from flask import Flask,render_template,request
from flask_wtf import Form
from flask_bootstrap import Bootstrap
from wtforms import FileField, SubmitField
from wtforms.validators import Required
from werkzeug.utils import secure_filename
from flask_pymongo import PyMongo


UPLOAD_FOLDER='static/images'
ALLOWED_EXTENSION=set(['pdf','png','jpg','jpeg','gif'])

app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['MONGO_DBNAME']='onceUponAPixel'
app.config['MONGO_URL']='mongodb://localhost:27017/onceUponAPixel'
app.secret_key='Some random secret key'
mongo=PyMongo(app)


Bootstrap(app)

class PhotoForm(Form):
	photo=FileField('Upload pictures', validators=[Required()])
	submit=SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
	information=mongo.db.info
	form=PhotoForm()
	if form.validate_on_submit():
		filename=secure_filename(form.photo.data.filename)
		form.photo.data.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		information.insert({'location':os.path.join(app.config['UPLOAD_FOLDER'],filename),'story':''})
	
	filename=None
	return render_template('upload.html',form=form,filename=filename)

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')