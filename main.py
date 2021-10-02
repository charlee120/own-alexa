import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(test):
    engine.say(test)
    engine.runAndWait()
def commands():
    try:
        with sr.Microphone() as source:
            print("lilith is listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ok' in command:
                command=command.replace('ok', '')
                print(command)

    except:
        pass
    return command
def run():
    command= commands()
    if 'play' in command:
        song = command.replace('play','')
        print('ok playing'+song)
        talk('ok. playing' + song)
        pywhatkit.playonyt('ok. playing' + song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('the current time is'+time)
    else:
        print('hay please say again')
        talk('hay please say again')
while True:
    run()
