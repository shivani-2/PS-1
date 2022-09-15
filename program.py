from pip._internal import main as pipmain

pipmain(['install', 'speechrecognition'])
pipmain(['install','pyaudio'])
pipmain(['install', 'pyttsx3'])

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
	
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	
	
# Loop infinitely for user to speak

print("Please speak ")
c=1
while(c==1):

	try:		

		with sr.Microphone() as source2:
			
			r.adjust_for_ambient_noise(source2, duration=0.2)
			audio2 = r.listen(source2)
			c = c + 1
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say "+MyText)
			SpeakText(MyText)
            
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occured")