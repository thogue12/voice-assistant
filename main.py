
import speech_recognition as sr
import playsound as playsound
from gtts import gTTS
import webbrowser
from time import ctime


r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source: 
         
        audio = r.listen(source)  
        voice_data =''
        try:  
            text = r.recognize_google(audio)  
            print(text)  
            
            
        except sr.UnknownValueError: 
            print("Sorry could not recognize what you said")
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print("My name is Bonquiqui")
    if 'what time is it' in voice_data:
        print(ctime())

print("How can i assist you?") 
voice_data = record_audio()
respond(voice_data)
