import speech_recognition as sr
import webbrowser as wb
import pyaudio
r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()
with sr.Microphone() as source:
    print("[Search google:search video]")
    print("Speak now......")
    audio=r1.listen(source)
if "search" in r1.recognize_google(audio):
    r2=sr.Recognizer()
    url="https://www.google.com/search?q="
    with sr.Microphone() as source:
        print("Search your query")
        audio=r2.listen(source)
        try:
            get=r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except:
            print("error")
if "video" in r1.recognize_google(audio):
    print("Search in you tube")
    r3=sr.Recognizer()
    url="https://www.youtube.com/results?search_query="
    with sr.Microphone() as source:
        print("Search your query")
        audio=r3.listen(source)
        try:
            get=r3.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except:
             print("error")
