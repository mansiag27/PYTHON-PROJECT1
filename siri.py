# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 14:47:49 2023

@author: Mansi Agarwal
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am gogo sir Please tell me how may I help you")
    

    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language ='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e :
        print(e)
        print("Say that again please....")
        return "None"
    return query
     
    
if __name__=="__main__":
   wishme()
   while True:
    query=takeCommand().lower()
   
    if 'wikipedia' in query:
       speak('Searching Wikipedia...')
       query=query.replace("wikipedia","")
       results=wikipedia.summary(query,sentences=2)
       speak("According to wikipedia")
       print(results)
       speak(results)
   
    elif 'open youtube' in query:
       webbrowser.open("youtube.com")
       
    elif 'open google' in query:
       webbrowser.open("google.com")
       
    elif 'the time' in query:
       strTime=datetime.datetime.now().strftime("%H:%M:%S")
       speak(f"Sir,the time is {strTime}")
       
    elif 'open the code' in query:
        codePath="C:\\Users\\hrsht\\Desktop\\waste.cpp"
        os.startfile(codePath)
        
    elif 'play music' in query:
        music_dir='C:\\Users\\hrsht\\Desktop\\music'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
        
   