import io
import os
import subprocess
import re
from subprocess import Popen, PIPE
import Split, FindVolume, FindBrightness, Rejoin, FindPitch, GetCommentator, ob, motion
import matplotlib.pyplot as plt
from pandas import DataFrame
import speech_recognition as sr
import os.path
from pathlib import Path

def audioAnalysis():

	volume_array = []
	pitch_array = []


	for filenames in os.listdir('audio'):
		vol = FindVolume.find_volume("audio/" + filenames)
		pitch = FindPitch.findFreq("audio/" + filenames)

		volume_array.append(vol)
		pitch_array.append(pitch)


	return volume_array, pitch_array

def commentaryAnalysis():

	#GetCommentator.StartCon()

	key_words = []
	path, dirs, files = next(os.walk("audio"))
	file_count = len(files)
	key_phrases = ('kick', 'goal', 'center', 'penalty', 'ball', 'foul', 'card', 'free')

	#r ' center' or 'penalty' or 'ball' or 'foul' or 'card' or 'free' 

	word_num_array = []

	print("Opens this folder")

	i = 0

	for i in range(file_count):
		key = False
		myfile = Path("text/speeches_" + str(i) + ".txt")
		if os.path.exists(myfile):
			#print("This file exists")
			data = open("text/speeches_" + str(i) + ".txt").read()
			wordcount = len(data.split())

			file = open("text/speeches_" + str(i) + ".txt", 'r')

			#Football
			for line in file.readlines():
				for word in key_phrases:
					if word in line:
						key = True

		else:
			#print("This file doesn't exist")
			wordcount = 0

		word_num_array.append(wordcount)
		key_words.append(key)

		i += 1

	return word_num_array, key_words


def frameAnalysis():
	bright_values = list(FindBrightness.find_brightness())
	return bright_values

def objectAnalysis():
	return(ob.findObject())

def motionAnalysis():
	return(motion.findImageChange()) 

def startAnalysis():

	#Initialise array with volume levels and brightness levels
	vol_arr = []
	bright_values = []
	pitch_arr = []
	key_arr = []
	wps_arr = []
	object_arr = []
	change_arr = []

	# bright_values = frameAnalysis()
	# wps_arr, key_arr = commentaryAnalysis()
	# vol_arr, pitch_arr = audioAnalysis()	

	bright_values = frameAnalysis()
	wps_arr, key_arr = commentaryAnalysis()
	vol_arr, pitch_arr = audioAnalysis()
	object_arr = objectAnalysis()
	change_arr = motionAnalysis()

	print(len(bright_values))
	print(len(wps_arr))
	print(len(key_arr))
	print(len(vol_arr))
	print(len(pitch_arr))
	print(len(object_arr))
	print(len(change_arr))

	Values = {'Brightness' : bright_values,
			  'Volume' : vol_arr,
			  'Pitch' : pitch_arr,
			  'Key_words' : key_arr,
			  'WPS' : wps_arr,
 			  'Object_found' : object_arr,
 			  'Change' : change_arr
		  }

	df = DataFrame(Values, columns = ['Brightness', 'Volume', 'Pitch', 'Key_words', 'WPS', 'Object_found', 'Change'])
	df.to_csv("football_10_second.csv")
#print(wps_arr)
#print(len(bright_values))

#print(len(wps_arr))
#print(len(key_arr))
#print(key_arr)
startAnalysis()
#print(len(vol_arr))

#print(len(pitch_arr))



# Values = {'Brightness' : bright_values,
# 			  'Volume' : vol_arr,
# 			  'Pitch' : pitch_arr,
# 			  'Key_words' : key_arr,
# 			  'WPS' : wps_arr,
#  			  'Object_found' : object_arr,
#  			  'Change' : change_arr
# 		  }

# df = DataFrame(Values, columns = ['Volume', 'Pitch', 'Key_words', 'WPS'])
# df.to_csv("football_10_second.csv")
