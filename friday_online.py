import pyttsx3
import speech_recognition as sr
import time
import random
import webbrowser
import os

engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

r = sr.Recognizer()


class Friday_online:

    @property
    def record(self):
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit=150)
            # noinspection PyShadowingNames
            voice = " "
            print(voice)
            try:
                # noinspection PyShadowingNames
                voice = r.recognize_google(audio, language="en-EN")
            except sr.UnknownValueError:
                engine.say("I don't Understand")
                engine.runAndWait()
            except sr.RequestError:
                engine.say("system is not working")
                engine.runAndWait()
            return voice

    def gelenses(self):

        if "hello Friday" in voice:
            speech1 = ["hello sir", "hi sir", "please sir"]
            engine.say(random.choice(speech1))
            engine.runAndWait()
        if "how are you" in voice:
            speech2 = ["I'm fine sir , you?", "good sir , you?"]
            engine.say(random.choice(speech2))
            engine.runAndWait()
        if "close" in voice:
            engine.say("okay sir")
            engine.runAndWait()
            exit()
        if "thank you" in voice:
            engine.say("you are welcome sir")
            engine.runAndWait()
        if "to search" in voice:
            engine.say("what am i sir?")
            engine.runAndWait()
            search = asistan.record
            url = "https://www.google.com/search?q={}".format(search)
            webbrowser.get().open(url)
            engine.say("{}what i found".format(search))
            engine.runAndWait()
        if "f*** you Friday" in voice:
            engine.say("no sir")
            engine.runAndWait()
        if "your creator" in voice:
            engine.say("to search sir")
            engine.runAndWait()
            time.sleep(3)
            url = "https://www.instagram.com/fazlenes/"
            webbrowser.get().open(url)
            engine.say("my creator")
            engine.runAndWait()
            time.sleep(3)
        if "wait Friday" in voice:
            engine.say("okay sir")
            engine.runAndWait()
            time.sleep(10)
        if "weather forecast" in voice:
            engine.say("okay sir")
            engine.runAndWait()
            webs = "https://www.google.com/search?q=hava+durumu+bornova"
            webbrowser.get().open(webs)
            engine.say("today is weather")
            time.sleep(0.5)
            engine.runAndWait()
        if "open application" in voice:
            engine.say("Which app should we open?")
            engine.runAndWait()
            runapp = asistan.record
            time.sleep(4)
            if "WhatsApp" in runapp:
                engine.say("okay sir")
                engine.runAndWait()
                os.startfile("C:\\Users\\AtesKusu\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            if "valorant" in runapp:
                engine.say("okay sir")
                engine.runAndWait()
                os.startfile("C:\\Users\\AtesKusu\\VALORANT.lnk")


engine.say("hello")
engine.runAndWait()
asistan = Friday_online()
while True:
    voice = asistan.record
    asistan.gelenses()
    print(voice)
