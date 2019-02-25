import speech_recognition as sr
import os

# def findSpeech():

# 	for file in os.listdir('audio'):
# 		ConvertAudio(file,)


def ConvertAudio(audio, x):

	with open("api-key.json") as f:
		GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

	#Add a path to the audio files
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))

	target = os.path.join(APP_ROOT, 'text/')

	if not os.path.isdir(target):
		os.mkdir(target)

	r = sr.Recognizer()

	with sr.AudioFile(audio) as source :
		r.adjust_for_ambient_noise(source)
		audio = r.record(source)

	try:
		#print("Mama mia")
		text = r.recognize_google_cloud(audio, credentials_json = GOOGLE_CLOUD_SPEECH_CREDENTIALS)

		file = open("text/speeches_" + str(x) + ".txt", "w+")

		file.write(text)

		file.close()

	except Exception as e:
		print(e)

#ConvertAudio("audio_output_0.wav", 0)

def StartCon():
	x = 0

	wordcount = []
	#word_detect = []
	
	for filenames in os.listdir('audio'):
		#print(filenames)
		if filenames.endswith(".wav"):
			#print(filenames)
			ConvertAudio('audio/' + filenames, x)
			x+=1

