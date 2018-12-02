from flask import Flask, render_template, redirect, request, stream_with_context, Response
from werkzeug import secure_filename
import os
import SplitFile


__author__ = 'Shona Doran'

app = Flask(__name__)

#DEBUG MODE _ REMOVE LATER
#app.debug = True

#Add the path of the uploaded video
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

#This will bind the url to the below function
@app.route('/')
def home():
	return render_template('upload.html')

@app.route('/upload', methods = ["GET", "POST"])
def upload():
	target = os.path.join(APP_ROOT, 'uploads/')
	print(target)

	#Add folder if it does not exist
	if not os.path.isdir(target):
		os.mkdir(target)

	#Get file and save to folder uploads
	f = request.files['up_file']
	destination = "/".join([target, f.filename])
	f.save(destination)
	ndestination = "/".join([target, 'upload.mp4'])


	#Tis will rename the file so the name will be irrelevant
	os.rename(destination, ndestination)

	#Break into segements and music segments
	SplitFile.split_video(ndestination)

	return redirect('/static/output.mp4')
	
if __name__ == '__main__' :
	app.run()

