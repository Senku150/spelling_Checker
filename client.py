import pyttsx3
import requests

engine = pyttsx3.init()


response = requests.get("http://192.168.1.10:5000")
word = response.text
print(word)
engine.say(word)
engine.runAndWait()
