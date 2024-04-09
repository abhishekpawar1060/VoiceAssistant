import pyttsx3 as p
import speech_recognition as sr
import randfacts

from selenium_web import infow
from YouTube import music
from News import news


engine = p.init()
rate = engine.getProperty('rate')  #Speed of the voice
engine.setProperty('rate',130) #change the speed rate to 180(default id 200)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)  #change the voice at 0 index male voice and 1 index female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()     #Recognizer use microphone

speak("Hello sir i'm your voice assistant. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000  #It increace the spectrum of voice
    r.adjust_for_ambient_noise(source, 1.2)  #cancle all noises around you
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("i am also having a good day sir")

speak("What can I do for you?")


with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.5)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2)

if "information" in text2:
    speak("You need information related to which topic")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.5)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)

    speak("Searching {} in wikipedia".format(infor))
    print("Searching {} in wikipedia".format(infor))

    assist = infow()
    assist.get_info(infor)
    assist.wait_to_close()

elif "play" and "video" in text2:
    speak("You want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.5)
        print("listening...")
        audio = r.listen(source)
        video = r.recognize_google(audio)

    speak("Playing {} in YouTube".format(video))
    print("Playing {} in YouTube".format(video))

    assist = music()
    assist.play(video)
    assist.wait_to_close()

elif "news" in text2:
    print("Sure sir, Now I will read news for you")
    speak("Sure sir, Now I will read news for you")

    arr = news()
    for i in range(len(arr)):
        speak(arr[i])
        print(arr[i])

elif "fact" or "facts" in text2:
    print("Sure sir ")
    speak("Sure sir ")

    x = randfacts.getFact()
    print(x)
    speak("Did you know that, "+x)