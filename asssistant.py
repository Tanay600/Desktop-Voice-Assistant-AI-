import pyttsx3  #is a text-to-speech conversion library in Python(run online/offline both)
import speech_recognition as sr      #library for speech recognition
import wikipedia
import datetime
import time
import webbrowser
import requests   #The requests module allows you to send HTTP requests using Python.
from bs4 import BeautifulSoup   #Beautiful Soup is a Python library for pulling data out of HTML and XML files.

#The Speech Application Programming Interface or SAPI is an API developed by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications.
#The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows.

engine = pyttsx3.init('sapi5') # init function to get an engine instance for the speech synthesis

voices = engine.getProperty('voices')  #Gets the current value of an engine property.

engine.setProperty('voice', voices[0].id)           #to set the voice



def speak(audio):          #audio is a string here

    engine.say(audio)            #pass input text to be spoken 
    engine.runAndWait()     #it processes the voice command



def WishFunc():         #WishFunc wishes the user according to the hour of the day

    hr = int(datetime.datetime.now().hour)             #took hour as an integer for if else

    type1 = input(" enter the command ") 

    if(type1 == "Okay Assis" or type1 == "Hey Assis"):        
        speak("Hey this is Assis, how can I help you")
    else:
        speak(" sorry, I can't understand ")

    time.sleep(1)                     #assistant takes the break here before saying the new line
    speak(" wish the Assis ")
    type2 = input(" wish me ")

    if(type2 == "Good Morning" or type2 == "Good Evening" or type2 == "Good Afternoon" or type2 == "Good Night"):


        if(hr>=0 and hr<12):
            speak("Good Morning User!, Have a great day ahead")

        elif(hr>=12 and hr<=16):
            speak("Good Afternoon User!")

        elif(hr>=17 and hr<=20):
            speak("Good Evening User!")

        else:
            speak("Good Night!, sweet dreams")  


def GiveCommand():                 #it takes the command from user

    r = sr.Recognizer()               #it recognizes the voice from the user

    with sr.Microphone() as source:     #sound recognize from the microphone
        print("Command Listening.........")
        r.pause_threshold = 1         #this function will make sure sentence will not be completed if user take 2 sec pause
        
        audio = r.listen(source)     #it will record the sentence phrase 


    try:
        print("Got it")

        query = r.recognize_google(audio, language='en-In')
        print(f"You mean : {query}\n")

    except Exception as e:
        #print(e)
        print("sorry, I can't understand, try again")
        return "None"
    return query      





if __name__ == "__main__":                        #main method

    WishFunc()
    while(True):
        query=GiveCommand().lower()

    # Internet task

        if "wikipedia" in query:                     #if there is wikipedia word in the query which user speaks or use
            speak("Searching Wikipedia...")          #then it will search with this text

            query = query.replace("wikipedia" , " ")          #and then replace the query with the details
            results = wikipedia.summary(query, sentences=2)   #wikipedia details will be there in summary
            speak("According to the Wikipedia ")
            print(results)
            speak(results)
        elif "open youtube" in query:

            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:

            speak("opening google")
            webbrowser.open("google.com")

        elif "open amazon" in query:

            speak("opening amazon")
            webbrowser.open("amazon.in") 

        elif "the time" in query:

            strtime = datetime.datetime.now().strtime("%H:%M:%S")   #tells hours minutes and seconds
            speak("the time is" , strtime) 

        elif "the weather" or "the temperature" in query:

            url = ("https://www.google.com/search?q=temperature in delhi")       #URL to achive the result
            r = requests.get(url)                            #store the data from given URL
            data = BeautifulSoup(r.text,"html.parser")  #web scrapping,Web scraping is the process
            # of using bots to extract content and data from a website.

            temp = data.find("div", class_="BNeawe").text 
            speak(f"current temperature is {temp}")
            print("the current temperature is " , temp) 


        
