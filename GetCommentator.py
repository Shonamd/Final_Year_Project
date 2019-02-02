import speech_recognition as sr
import os

dire = 'audio'

def ConvertAudio(audio, x):
	r = sr.Recognizer()

	with sr.AudioFile(audio) as source :
		audio = r.record(source)

	try:
		text = r.recognize_google(audio)

		file = open("text/speeches_" + str(x) + ".txt", "w+")

		file.write(text)

		file.close()

		print("worked")

		data = open("text/speeches_" + str(x) + ".txt", 'r').read()

		wordcount = len(data.split())

		print(wordcount)

		#return(text)

	except Exception as e:
		print(e)

# for x in range(3):
# 	ConvertAudio('audio/audio_output_' + str(x + 10) + '.wav')



#ConvertAudio('audio/audio_output_20.wav', 0)

def StartCon():
	x = 0
	
	for filenames in os.listdir('audio'):
		if filenames.endswith(".wav"):
			#print(filenames)
			ConvertAudio('audio/'+filenames, x)
			x += 1

			
def findKeyWord(file):
	if 'drive' in open(file).read():
		print("true")

StartCon()

# for filenames in os.listdir(dire):
# 	print(filenames)

# 	#add_clips()

# 	ConvertAudio(dire + '/' + filenames, x)



	#print("\n")
