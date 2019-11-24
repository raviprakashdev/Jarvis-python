import pyttsx3   #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia  #pip install wikipedia
import webbrowser
import os

# install pipwin
# pipwin install pyaudio 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


# functions
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Evening!")

    else:
        speak("good evening ")
    speak("I am jarvis. Please tell me how can i help you Ravi sir")

def takeCommand():
    # it takes mic input from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_thresold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query

    
# main funtions
if __name__ == "__main__":
    # speak("ravi is a very good boy")
    wishMe()
    while True:
        query = takeCommand().lower()
    # logic for executing tasks based on qwery

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif  'play music' in query:
            music_dir = 'E:\\raviprakash\\E\\songs\\BHAJAN'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[5]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Program Files\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)

        elif 'kill' in query:
            speak("bye sir")
            exit()


        # TODO send email
