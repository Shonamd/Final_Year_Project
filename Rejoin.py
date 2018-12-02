import io
import os
import subprocess

def Rejoin(volume, bright):

	volume_vals = volume
	bright_vals = bright

	peak_arr = []

	for i in range(len(volume_vals)):
		if abs(volume_vals[i] - bright_vals[i]) < 20:
			peak_arr.append(i)

	print(peak_arr)

	find_clips(peak_arr)	


def find_clips(join):
	file = open("join.txt", "w+")

	for i in range(len(join)):
		file.write("file \'visual/video_output_" + str(join[i]) +".mp4\' \n")

	file.close()

	add_clips()

def add_clips():

	#Add a path to the audio files
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))

	target = os.path.join(APP_ROOT, 'static/')

	if not os.path.isdir(target):
		os.mkdir(target)

	#command = "ffmpeg -safe 0 -f concat -i join.txt -c copy output.mp4"
	#command = "ffmpeg -f concat -safe 0 -i join.txt -c copy "+ target + "/output.mp4"

	command = "ffmpeg -safe 0 -f concat -i join.txt -c copy " + target +"output.mp4"
	subprocess.call(command,shell=True)

add_clips()


#Rejoin([0, 1, 21, 5], [0, 2, 3, 3])
