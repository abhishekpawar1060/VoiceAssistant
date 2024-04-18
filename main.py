import pyttsx3 as py
import speech_recognition as sr
import randfacts
import datetime

from selenium_web import infow
from YouTube import music
from News import news
from jokes import *
from weather import *
from wishme import *
from gemini import gemini

engine = py.init()
rate = engine.getProperty('rate')  #Speed of the voice
engine.setProperty('rate',130) #change the speed rate to 180(default id 200)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)  #change the voice at 0 index male voice and 1 index female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

today_date = datetime.datetime.now()
r = sr.Recognizer()     #Recognizer use microphone

speak("Hello sir, Good " +wish()+ " i'm your voice assistant.")
speak("How are You?")

with sr.Microphone() as source:
    r.energy_threshold = 10000  #It increace the spectrum of voice
    r.adjust_for_ambient_noise(source, 1.2)  #cancle all noises around you
    print("listening")
    audio = r.listen(source)
    text_found = False
    while not text_found:
        text = r.recognize_google(audio)
        text_found = True

    print(text)

if "what" and "about" and "you" in text:
    speak("I am also having a good day sir")

first = True

while True:
    if first:
        first = False
        speak("What can I do for you?")
    else:
        speak("Anything else I can help you with?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.5)
        print("listening...")
        audio = r.listen(source)
        text_found = False
        while not text_found:
            try:
                text2 = r.recognize_google(audio)
                text_found = True
            except:
                speak("Please repeat!")
                print("Please repeat!")
        print(text2)

    if "information" in text2:
        speak("You need information related to which topic?")
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
            print(arr[i])
            speak(arr[i])

    elif "fact" in text2:
        print("Sure sir ")
        speak("Sure sir ")

        x = randfacts.get_fact()
        print(x)
        speak("Did you know that, "+x)


    elif "joke" in text2:
        print("Sure sir")
        speak("Sure sir")

        arr = joke()
        print(arr[0])
        speak(arr[0])
        print(arr[1])
        speak(arr[1])


    elif "weather" in text2:
        print("Sure sir")
        speak("Sure sir")
        print("Temperature in Aurangabad is "+str(temp())+" degree celcius" " and with " +str(des()))
        speak("Temperature in Aurangabad is " + str(temp()) + " degree celcius" " and with " + str(des()))

    elif "time" in text2:
        print("Sure sir")
        speak("Sure sir")
        print("Today is "+today_date.strftime("%d")+ " of " +today_date.strftime("%B")+ " And its currenty " +(today_date.strftime("%I:"))+(today_date.strftime("%M"))+" ")
        speak("Today is " + today_date.strftime("%d") + " of" + today_date.strftime("%B") + " And its currenty " + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%D")))

    else:
        if "no thanks" in text2:
            exit()

        response = gemini(text2)
        print(response)
        speak(response)