import wikipedia
import pyttsx3


def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def chat(text):
    result = wikipedia.summary(text, sentences=1)
    if result:
        say(result)


while True:
    chat(input(': '))
