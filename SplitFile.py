import io
import os
import subprocess
import re
from subprocess import Popen, PIPE
import Split, FindVolume, FindBrightness, Rejoin, FindPitch, GetCommentator, ob, motion, getAudioFiles
import matplotlib.pyplot as plt
import analysis
from pandas import DataFrame
from multiprocessing.dummy import Pool


pool = Pool(8)

def find_time(video) :
	#This will call a command that will find the duration of the video
	command_time = "ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 " + video
	#This will call the command using python
	proc=subprocess.Popen(command_time, shell=True, stdout=subprocess.PIPE, )
	#This will return the output of the command (the duration) but will return it as a byte object
	x=proc.communicate()[0]
	#print(type(x))
	#This will change the byte object to a string
	a = "".join(map(chr, x))
	#print(type(a))
	#This will remove uncessary remains from the byte oject and return the time in seconds as an integer
	x = int(re.search(r'\d+', a).group())
	#print(type(x))
	#print("Time is  " + str(x))
	return x

def extract_audio(video, x):

	#Add a path to the audio files
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))

	target = os.path.join(APP_ROOT, 'audio/')

	if not os.path.isdir(target):
		os.mkdir(target)

	audio_command = "ffmpeg -i " + video +" -vn "+ target +"/audio_output_"+str(x)+".wav"
	subprocess.call(audio_command,shell=True)

def nextSplit():
	getAudioFiles.getAudio()
	Split.splitFrames()	


def splitVideo(video, x, i):
	#print("Calls")
	command = "ffmpeg -i " + video + " -vcodec copy -acodec copy -ss " +  str(i) +  " -t 00:00:10 visual/video_output_" + str(x) +".mp4"
	subprocess.call(command,shell=True)


def split_video(video) :

	#Add the path of the uploaded video
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))

	target = os.path.join(APP_ROOT, 'visual/')

	if not os.path.isdir(target):
		os.mkdir(target)


	i = 0 

	time = find_time(video)

	#For 10 seconds
	#num_seg = int(time/10)
	#For 5 seconds
	num_seg = int(time/5)

	for x in range(0, num_seg-1) :
		pool.apply_async(splitVideo, (video, x, i))
		#For 10 seconds
		#i = i + 10
		#For 5 seconds
		i = i + 5

	pool.close()
	pool.join()

	nextSplit()

	#getAudioFiles.getAudio()
	#Split.splitFrames()


	#analysis.startAnalysis()



split_video("footballtest.mp4")
