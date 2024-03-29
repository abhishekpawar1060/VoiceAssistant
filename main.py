import pyttsx3 as p
import speech_recognition as sr

engine = p.init()
rate = engine.getProperty('rate')  #Speed of the voice
engine.setProperty('rate',130) #change the speed rate to 180(default id 200)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)  #change the voice at 0 index male voice and 1 index female voice
engine.say("hello there is am your voice assistant")
engine.runAndWait()

r = sr.Recognizer()     #Recognizer use microphone

with sr.Microphone() as source:
    r.energy_threshold = 10000  #It increace the spectrum of voice
    r.adjust_for_ambient_noise(source, 1.2)  #cancle all noises around you
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)


