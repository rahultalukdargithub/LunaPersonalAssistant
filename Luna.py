from colorsys import yiq_to_rgb
from hashlib import new
from multiprocessing.spawn import _main
from pickle import TRUE
from re import M
from tkinter.tix import MAIN
from googletrans import Translator
from more_itertools import take
from pip import main
import pyperclip
import pyttsx3
import datetime
import speech_recognition as sr
from sqlalchemy import true
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
import pywhatkit
from pywikihow import  search_wikihow
from GoogleImageScrapper.GoogleImageScrapper import GoogleImageScraper
import pyautogui
from instadownloader import instaloader
import time
import wolframalpha
import psutil
import speedtest
import cv2
from twilio.rest import Client
from playsound import playsound
import pyjokes
from googletrans import Translator
from pyautogui import click
from pyautogui import hotkey
from pyperclip import paste
from pytube import YouTube
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from PIL import Image
import random
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate',160)


search = "temperature in my location"
url = f"https://www.google.com/search?q={search}"
r = requests.get(url)
data = BeautifulSoup(r.text, "html.parser")
# temp=data.find("div",class_="BNeawe").text
# get the temperature
temp = data.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

# this contains time and sky description
sta = data.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# format the data
data = sta.split('\n')
Time = data[0]
t=str(Time)
s=t.split()
day=s[0]
T=s[1]
m=s[2]
sky = data[1]

# speak(f"current{search} is {temp}")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    # speak("Hi ,I am jarvis")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("For you sir, always. Good morning sir! ")
        speak(f"its {Time} ,currently {sky} outside")
    elif hour >= 12 and hour < 18:
        speak(" For you sir, always. Good afternoon !")
        speak(f"its {Time} ,currently {sky} outside")
    else:
        speak(" For you sir, always. Good evening sir! ")
        speak(f"its {Time} ,currently {sky} outside")
    speak(" Tell me how can i help you")

def takecommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()  # it will help to recognize the input
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1.5
        audio = r.listen(source, timeout=3, phrase_time_limit=10)
    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        # print("user said: \n", query)

    except Exception as e:
        print("say that again please....")
        speak("say that again please")
        return "None"
    return query

def wolFrame(query):
    api_key = "ETP576-PA39EWHY7Q"
    requester = wolframalpha.Client(api_key)
    requested=requester.query(query)
    try:
        ans = next(requested.results).text
        print(ans)
        speak(ans)
        return ans
    except:
        # speak("nothing found !")  
        speak("hold on")
        pywhatkit.search(query)
        speak("here is the solution of your problem")  

def GoogleSearch(term):
    
    query = term.replace("do you know about","")
    query = term.replace("who is","")
    query = term.replace("how to","")
    query = term.replace("what do you mean by","")
    
    writeab= str(query)
    
    data=open('database.txt','a')
    data.write(writeab)
    data.close()
    Query=str(term)
    pywhatkit.search(writeab)
    if 'how to' in query:
        max_result = 1
        how_to = search_wikihow(Query,max_result)
        assert len(how_to)==1
        how_to[0].print()
        speak(how_to[0].summary)
    else:
        results2 = wikipedia.summary(writeab, sentences=2)
        print(results2)
        # speak("according to wikipedia")
        speak(results2)
    speak("You can see some pictures from google, as well . ")    
    GoogleImage()    

def GoogleImage():
    nm = open('C:\\Users\\Rahul Talukdar\\Desktop\\final\\database.txt','rt')
    query = str(nm.read())
    nm.close()
    dele = open('C:\\Users\\Rahul Talukdar\\Desktop\\final\\database.txt','r+')
    dele.truncate(0)
    dele.close()

    webdriver = "C:\\Users\\Rahul Talukdar\\Desktop\\final\\web driver\\chromedriver.exe"
    photos = "C:\\Users\\Rahul Talukdar\\Desktop\\final\\google photos"

    search_keys = query
    number = 10
    head = False
    max = (1000,1000)
    min = (0,0)

    # for search_key in search_keys:
    image_search = GoogleImageScraper(webdriver,photos,search_keys,number,head,min,max)
    image_url = image_search.find_image_urls()
    image_search.save_images(image_url)
    speak("I have also downloaded some pictures for you . You can see it in your google photos folder . ")
    speak("Here you go sir!")
    os.startfile(photos)    
# GoogleImage()

def news():
    # api_key=ac4f72ed084f45cabb2fffb521196280
    main_url= 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=ac4f72ed084f45cabb2fffb521196280'
    main_page=requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"today's {day[i]} news is: {head[i]}")
        speak(f"today's {day[i]} news is: {head[i]}")    

def takecommandinhindi():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()  # it will help to recognize the input
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1.5
        audio = r.listen(source, timeout=3, phrase_time_limit=10)
    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='hi-in')
        # print("user said: \n", query)

    except Exception as e:
        print("say that again please....")
        speak("say that again please")
        return "None"
    return query

def DownloadYoutube():
    time.sleep(3)
    speak("Wait sir.")
    click(x=905, y=76)
    hotkey('ctrl','c')
    value=pyperclip.paste()
    link=str(value)
    url=YouTube(link)
    video=url.streams.first()
    video.download("C:\\Users\\Rahul Talukdar\\Desktop\\prog\\final\\YouTube")
    speak("sir, i have downloaded this video for in YouTube folder.")

def YouTubeAuto():
    while True:
        command=takecommand().lower()
        query = str(command)
        if 'pause' in query:
            press('space bar')
        elif 'resume' in query:
            press('space bar')
        elif 'full screen' in query:
            press('f')
        elif 'film screen' in query:
            press('t')
        elif 'skip' in query:
            press('l')
        elif 'back' in query:
            press('j')
        elif 'increase' in query:
            press_and_release('SHIFT + .')
        elif 'decrease' in query:
            press_and_release('SHIFT + ,')
        elif 'previous' in query:
            press_and_release('SHIFT + p')
        elif 'next' in query:
            press_and_release('SHIFT + n')
        elif 'search' in query:
            click(x=923, y=117)
            speak("What To Search Sir ?")
            search = takecommand()
            write(search)
            time.sleep(0.8)
            press('enter')
        elif 'download' in query:
            DownloadYoutube()    
        elif 'mute' in query:
            press('m')
        elif 'unmute' in query:
            press('m')
        elif 'new tab' in query:
            press_and_release('ctrl + t')
        elif 'close tab' in query:
            press_and_release('ctrl + w')
        elif 'new window' in query:
            press_and_release('ctrl + n')
        elif 'history' in query:
            press_and_release('ctrl + h')
        elif 'download' in query:
            press_and_release('ctrl + j')
        elif 'bookmark' in query:
            press_and_release('ctrl + d')
            press('enter')
        elif 'incognito' in query:
            press_and_release('Ctrl + Shift + n')
        elif 'switch tab' in query:
            tab = query.replace("switch tab ", "")
            Tab = tab.replace("to","")
            num = Tab
            bb = f'ctrl + {num}'
            press_and_release(bb)
        elif 'previously closed tabs' in query:
            press_and_release('Ctrl + Shift + t')
        elif 'next tab' in query:
            press_and_release('Ctrl + Tab')
        elif 'previous tab' in query:
            press_and_release('Ctrl + PgUp')
        elif 'home page in the current tab' in query:
            press_and_release('Alt + Home')
        elif 'previous page' in query:
            press_and_release('Alt + Left arrow')
        elif 'next page' in query:
            press_and_release('Alt + Right arrow')
        elif 'Close the tab' in query:
            press_and_release('Ctrl + w')
        elif 'Close the current window' in query:
            press_and_release('Ctrl + Shift + w')
        elif 'address bar' in query:
            press_and_release('Ctrl + l')
        elif 'Search here' in query:
            press_and_release('Ctrl + k')
        elif 'down' in query:
            press('PgDn')
        elif 'up' in query:
            press('PgUp')
        elif 'go to the top of the page' in query:
            press('Home')
        elif 'go to the bottom of the page' in query:
            press('End')
        elif 'print the current page' in query:
            press_and_release('Ctrl + p')
        elif 'save the current page' in query:
            press_and_release('Ctrl + s')
        elif 'reload' in query:
            press_and_release('Ctrl + r')
        elif 'tap' in query:
            press('Tab')
        elif 'go back' in query:
            press_and_release('Shift + Tab')
        elif 'a file' in query:
            press_and_release('Ctrl + o')
        elif 'full-screen' in query:
            press('F11')
        elif 'zoom in' in query:
            press_and_release('Ctrl and +')
        elif 'zoom out' in query:
            press_and_release('Ctrl and -')
        elif 'normal' in query:
            press_and_release('Ctrl + 0')
        elif 'open it' in query or 'go on' in query or 'search' in query or 'click' in query or 'enter' in query:
            press('enter')    
        elif 'write' in query:
            query=query.replace("write","")
            pyautogui.write("query")
        elif 'previous word' in query:
            press_and_release('Ctrl + Left arrow')
        elif 'next word' in query:
            press_and_release('Ctrl + Right arrow')
        elif 'delete the word' in query:
            press_and_release('Ctrl + Backspace')
        elif 'copy' in query:
            press_and_release('Ctrl + c')  
        elif 'paste' in query:
            press_and_release('Ctrl + v')
        elif 'switch ' in query:
            press_and_release('Alt + Tab')    
        elif 'close' in query:
            press_and_release('Alt + F4') 
            break
        elif 'restore' in query:
            press_and_release('Windows + Down arrow') 
        elif 'maximize' in query:
            press_and_release('Windows + Up Arrow')
        elif 'minimize' in query:
            press_and_release('Windows + Up Arrow')
            time.sleep(2)
            click(x=1791, y=18) 
        elif 'minimize all' in query:
            press_and_release('Windows + M')
        elif 'go to the taskbar' in query:
            press_and_release('Windows + T')
        elif 'no' in query or 'go ahead' in query:
            press('Right arrow')
        elif 'back' in query:
            press('Left arrow') 
       
def WhatsappMsg(name):
    Whatsappchat(name)
    click(x=1143, y=995)
    time.sleep(1)
    speak("what to send?")
    msg=takecommand().lower()
    pyautogui.write(msg)
    pyautogui.press('enter')
    whatsappauto()

def WhatsappCall(name):
    Whatsappchat(name)
    click(x=1735, y=78)

def WhatsappVCall(name):
    Whatsappchat(name)
    click(x=1659, y=85)

def Whatsappchat(name):
    os.startfile("C:\\Users\\Rahul Talukdar\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    time.sleep(20)
    click(x=302, y=143)
    time.sleep(1)
    pyautogui.write(name)
    time.sleep(1)
    click(x=332, y=305)
    time.sleep(1)
    
def whatsappauto():
    while True:
        query = takecommand().lower()
        if 'search' in query:
            press_and_release('CTRL + F')
        elif 'mark as unread' in query:
            press_and_release('CTRL + SHIFT + U')
        elif 'archive chat' in query:
            press_and_release('CTRL + E')
        elif 'pin' in query or 'unpin' in query:
            press_and_release('CTRL + SHIFT + P')
        elif 'search in chat' in query:
            press_and_release('CTRL + SHIFT + F')
        elif 'new group' in query:
            press_and_release('CTRL + SHIFT + N')    
        elif 'settings' in query:
            press_and_release('CTRL + ,')
        elif 'Mute Chat' in query:
            press_and_release('CTRL + SHIFT + M')
        elif 'Delete Chat' in query:
            press_and_release('CTRL + SHIFT + D')
        elif 'New Chat' in query:
            press_and_release('CTRL + N')
        elif 'Open Profile' in query:
            press_and_release('CTRL + P')
        elif 'videocall' in query:
            query=query.replace("videocall to ","")
            WhatsappVCall(query)
        elif 'voicecall' in query:
            query=query.replace("voicecall to ","")
            WhatsappCall(query)
        elif 'type' in query or 'write' in query:
            query=query.replace("type","")
            pyautogui.write(query)
        elif 'tap' in query:
            press('Tab')
        elif 'go back' in query:
            press_and_release('Shift + Tab')
        elif 'search' in query or 'send' in query or 'open' in query:
            press('enter')                                                       
        elif 'previous word' in query:
            press_and_release('Ctrl + Left arrow')
        elif 'next word' in query:
            press_and_release('Ctrl + Right arrow')
        elif 'delete the word' in query:
            press_and_release('Ctrl + Backspace')
        elif 'copy' in query:
            press_and_release('Ctrl + c')  
        elif 'paste' in query:
            press_and_release('Ctrl + v')
        elif 'select to left' in query:
            press_and_release('Shift + Left arrow')
            kki=takecommand().lower()
            if "select" in kki:
                press_and_release('Shift + Left arrow')
            elif "ok" in kki:
                break   
        elif 'select to right' in query:
            press_and_release('Shift + Right arrow')
            kki=takecommand().lower()
            if "select" in kki:
                press_and_release('Shift + Right arrow')
            elif "ok" in kki:
                break      
        elif 'switch window' in query:
            press_and_release('Alt + Tab')    
        elif 'close' in query:
            press_and_release('Alt + F4') 
            break
        elif 'restore' in query:
            press_and_release('Windows + Down arrow') 
        elif 'maximize' in query:
            press_and_release('Windows + Up Arrow')
        elif 'minimize' in query:
            press_and_release('Windows + Up Arrow')
            time.sleep(2)
            click(x=1791, y=18)
        elif 'minimize all' in query:
            press_and_release('Windows + M')
        elif 'go to the taskbar' in query:
            press_and_release('Windows + T')
        elif 'no' in query or 'go ahead' in query:
            press('Right arrow')
        elif 'back' in query:
            press('Left arrow') 
        elif 'up' in query:
            press('Up Arrow')
        elif 'down' in query:
            press('Down Arrow')       

def ChromeAuto():
    while true:
        query = takecommand().lower()
        if 'new tab' in query:
            press_and_release('ctrl + t')
        elif 'close tab' in query:
            press_and_release('ctrl + w')
        elif 'new window' in query:
            press_and_release('ctrl + n')
        elif 'history' in query:
            press_and_release('ctrl + h')
        elif 'download' in query:
            press_and_release('ctrl + j')
        elif 'bookmark' in query:
            press_and_release('ctrl + d')
            press('enter')
        elif 'incognito' in query:
            press_and_release('Ctrl + Shift + n')
        elif 'switch tab' in query:
            tab = query.replace("switch tab ", "")
            Tab = tab.replace("to","")
            num = Tab
            bb = f'ctrl + {num}'
            press_and_release(bb)
        elif 'previously closed tabs' in query:
            press_and_release('Ctrl + Shift + t')
        elif 'next tab' in query:
            press_and_release('Ctrl + Tab')
        elif 'previous tab' in query:
            press_and_release('Ctrl + PgUp')
        elif 'home page in the current tab' in query:
            press_and_release('Alt + Home')
        elif 'previous page' in query:
            press_and_release('Alt + Left arrow')
        elif 'next page' in query:
            press_and_release('Alt + Right arrow')
        elif 'Close the tab' in query:
            press_and_release('Ctrl + w')
        elif 'Close the current window' in query:
            press_and_release('Ctrl + Shift + w')
        elif 'address bar' in query:
            press_and_release('Ctrl + l')
        elif 'Search here' in query:
            press_and_release('Ctrl + k')
        elif 'down' in query:
            press('PgDn')
        elif 'up' in query:
            press('PgUp')
        elif 'go to the top of the page' in query:
            press('Home')
        elif 'go to the bottom of the page' in query:
            press('End')
        elif 'print the current page' in query:
            press_and_release('Ctrl + p')
        elif 'save the current page' in query:
            press_and_release('Ctrl + s')
        elif 'reload' in query:
            press_and_release('Ctrl + r')
        elif 'tap' in query:
            press('Tab')
        elif 'go back' in query:
            press_and_release('Shift + Tab')
        elif 'a file' in query:
            press_and_release('Ctrl + o')
        elif 'full-screen' in query:
            press('F11')
        elif 'select to left' in query:
            press_and_release('Shift + Left arrow')
            kki=takecommand().lower()
            if "select" in kki:
                press_and_release('Shift + Left arrow')
            elif "ok" in kki:
                break   
        elif 'select to right' in query:
            press_and_release('Shift + Right arrow')
            kki=takecommand().lower()
            if "select" in kki:
                press_and_release('Shift + Right arrow')
            elif "ok" in kki:
                break    
        elif 'zoom in' in query:
            press_and_release('Ctrl and +')
        elif 'zoom out' in query:
            press_and_release('Ctrl and -')
        elif 'normal' in query:
            press_and_release('Ctrl + 0')
        elif 'open it' in query or 'go on' in query or 'search' in query or 'click' in query or 'enter' in query:
            press('enter')    
        elif 'write' in query:
            query=query.replace("write","")
            pyautogui.write("query")
        elif 'previous word' in query:
            press_and_release('Ctrl + Left arrow')
        elif 'next word' in query:
            press_and_release('Ctrl + Right arrow')
        elif 'delete the word' in query:
            press_and_release('Ctrl + Backspace')
        elif 'copy' in query:
            press_and_release('Ctrl + c')  
        elif 'paste' in query:
            press_and_release('Ctrl + v')
        elif 'switch window' in query:
            press_and_release('Alt + Tab')    
        elif 'close' in query:
            press_and_release('Alt + F4') 
            break
        elif 'restore' in query:
            press_and_release('Windows + Down arrow') 
        elif 'maximize' in query:
            press_and_release('Windows + Up Arrow')
        elif 'minimize' in query:
            press_and_release('Windows + Up Arrow')
            time.sleep(2)
            click(x=1791, y=18) 
        elif 'minimize all' in query:
            press_and_release('Windows + M')
        elif 'go to the taskbar' in query:
            press_and_release('Windows + T')
        elif 'no' in query or 'go ahead' in query:
            press('Right arrow')
        elif 'back' in query:
            press('Left arrow')        
        elif 'open' in query or 'show' in query:
            name = query.replace("open ","")
            NameA = str(name)
            if 'youtube' in NameA:
                webbrowser.open("https://www.youtube.com/")
                speak("would you like to handle it on your own?")
                lt=takecommand().lower()
                if 'no' in lt:
                    YouTubeAuto()
                else:
                    pass
            elif 'instagram' in NameA:
                webbrowser.open("https://www.instagram.com/")
                ChromeAuto()
            else:
                string = "https://www." + NameA + ".com"
                string_2 = string.replace(" ","")
                webbrowser.open(string_2)
                ChromeAuto()

def DateConverter(query):
    query = query.replace(" and ","-")
    query = query.replace("and","-")
    query = query.replace(" ","")
    return str(query)

def MarsImage():
    name = 'curiosity' 
    date = '2021-12-3'
    Api_Key = "ogzOxkpRcIzSxXR8lZ3XS6aBb3ZkAUGphyUhOUch" 
    # date = '2020-12-3'
    Api_ = str(Api_Key)
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"
    r = requests.get(url)
    Data = r.json()
    # speak("how many pictures do you want?")
    # pic=takecommand().lower()
    Photos = Data['photos'][:6]
    try:
        for index , photo in enumerate(Photos):
            camera = photo['camera']
            full_camera_name = camera['full_name']
            date_of_photo = photo['earth_date']
            img_url = photo['img_src']
            p = requests.get(img_url)
            img = f'{index}.jpg'
            t=str(img)
            with open(img,'wb') as file:
                file.write(p.content)
            Path_1 = f"C:\\Users\\Rahul Talukdar\\Desktop\\prog\\final\\{t}"
            Path_2 = f"C:\\Users\\Rahul Talukdar\\Desktop\\prog\\final\\MARS\\{t}"
            os.rename(Path_1,Path_2)
            os.startfile(Path_2)
            speak(f"This Image Was Captured With : {full_camera_name}")
            speak(f"This Image Was Captured On : {date_of_photo}")
    except:
        speak("There IS An Error!")

def NasaNews(Date):
    Api_Key = "ogzOxkpRcIzSxXR8lZ3XS6aBb3ZkAUGphyUhOUch"
    speak("Extracting Data From Nasa . ")
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
    Params = {'date':str(Date)}
    r = requests.get(Url,params = Params)
    Data = r.json()
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    Image_r = requests.get(Image_Url)
    FileName = str(Date) + '.jpg'
    with open(FileName,'wb') as f:
        f.write(Image_r.content)
    x=str(FileName)    
    Path_1 = f"C:\\Users\\Rahul Talukdar\\Desktop\\prog\\final\\{x}"
    Path_2 = f"C:\\Users\\Rahul Talukdar\\Desktop\\prog\\final\\NASA\\{x}"
    os.rename(Path_1, Path_2)
    img = Image.open(Path_2)
    img.show()
    speak(f"Title : {Title}")
    speak(f"According To Nasa : {Info}")

def Summary(Boby):
    name = str(Boby)
    url = f"https://hubblesite.org/api/v3/glossary/{name}" 
    r = requests.get(url)
    Data = r.json()
    if len(Data) != 0:
        retur =  Data['definition']
        speak(f"According To The Nasa : {retur}")
    else:
        speak("No Data Available , Try Again Later!")

def Astro(start_date,end_date):
    Api_Key = "ogzOxkpRcIzSxXR8lZ3XS6aBb3ZkAUGphyUhOUch"
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"
    r = requests.get(url)
    Data = r.json()
    Total_Astro = Data['element_count']
    neo = Data['near_earth_objects']
    speak(f"Total Astroid Between {start_date} and {end_date} Is : {Total_Astro}")
    speak("let me tell you some  Data related to Those Astroids.")
    for body in neo[start_date]:
        id = body['id']
        name = body['name']
        print(f"name : {name}")
        speak(f"name {name}")
        absolute = body['absolute_magnitude_h']
        print(f"it's absolute magnitude was : {absolute}")
        speak(f"it's absolute magnitude was {absolute}")
        estimated_diametermax=body['estimated_diameter']['kilometers']['estimated_diameter_max']
        print(f"it's estimated maximum diameter was :  {estimated_diametermax}  kilometers")
        speak(f"it's estimated maximum diameter was {estimated_diametermax}  kilometers")
        estimated_diametermin=body['estimated_diameter']['kilometers']['estimated_diameter_min']
        print(f"it's estimated minimum diameter was :  {estimated_diametermin} kilometers")
        speak(f"it's estimated minimum diameter was {estimated_diametermin} kilometers")
        # hazardous=body["is_potentially_hazardous_asteroid"]
        if(body["is_potentially_hazardous_asteroid"]==True):
            speak("It was potentially hazardous")
        # print(id,name,absolute,estimated_diametermax,estimated_diametermax)

def solarbodies(body):
    url="https://api.le-systeme-solaire.net/rest/bodies/"
    r=requests.get(url)
    data =r.json()
    bodies=data['bodies']
    # number=len(bodies)
    url_2=f"https://api.le-systeme-solaire.net/rest/bodies/{body}"
    rrr=requests.get(url_2)
    data_2 =rrr.json()
    discoveryDate=data_2['discoveryDate']
    speak(f"{body} was discovered first in {discoveryDate}")
    mass=data_2['mass']['massValue']
    massexpo=data_2['mass']['massExponent']
    speak(f"it's mass is {mass} into ten to the power {massexpo} kilograms")
    volume=data_2['vol']['volValue']
    volumeexpo=data_2['vol']['volExponent']
    speak(f"it's volume is {volume} into ten to the power {volumeexpo} kilometre cube")
    density=data_2['density']
    speak(f"it's density is {density} gram per centimeter cube")
    gravity=data_2['gravity']
    speak(f"it's gravity is {gravity} meters per second square")
    escape=data_2['escape']
    speak(f"it's escape velocity is {escape} meters per second")
    avgTemp=data_2['avgTemp']
    speak(f"it's average temperature is {avgTemp} degrees Kelvin")

Hello = ('hello','hey','hii','hi')

reply_Hello = ('Hello Sir , I Am Jarvis .',
            "Hey , What's Up ?",
            "Hey How Are You ?",
            "Hello Sir , Nice To Meet You Again .",
            "Of Course Sir , Hello .")

Bye = ('bye','exit','sleep','go')

reply_bye = ('Bye Sir.',
            "It's Okay .",
            "It Will Be Nice To Meet You .",
            "Bye.",
            "Thanks.",
            "Okay.")

How_Are_You = ('how are you','are you fine')

reply_how = ('I Am Fine.',
            "Excellent .",
            "Moj Ho rhi Hai .",
            "Absolutely Fine.",
            "I'm Fine.",
            "Thanks For Asking.I Am Fine.")

nice = ('nice','good','thanks')

reply_nice = ('Thanks .',
            "Ohh , It's Okay .",
            "Thanks To You.")

Functions = ('functions','abilities','what can you do','features')

reply_Functions = ('I Can Perform Many Task Or Varieties Of Tasks , How Can I Help You ?',
            'I Can Call Your G.F .',
            'I Can Message Your Mom That You Are Not Studing..',
            'I Can Tell Your Class Teacher That You Had Attended All The Online Classes On Insta , Facebbook etc!',
            'Let Me Ask You First , How Can I Help You ?',
            'If You Want Me To Tell My Features , Call : Print Features !')

sorry_reply = ("Sorry , That's Beyond My Abilities .",
                "Sorry , I Can't Do That .",
                "Sorry , That's Above Me.","Repeat it again correctly.")

def ChatterBot(Text):
    # Text = str(Text)
    # for word in Text.split():
        if Text in Hello:
            reply = random.choice(reply_Hello)
            return reply
        elif Text in Bye:
            reply = random.choice(reply_bye)
            return reply
        elif Text in How_Are_You:
            reply_ = random.choice(reply_how)
            return reply_
        elif Text in nice:
            reply=random.choice(reply_nice)  
            return reply  
        elif Text in Functions:
            reply___ = random.choice(reply_Functions)
            return reply___
        else:
            return random.choice(sorry_reply)

def GoogleMaps(Place):
    Url_Place = f"https://www.google.com/maps/place/{Place}"
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(Place , addressdetails= True)
    target_latlon = location.latitude , location.longitude
    speak("wait sir, i'm searching.")
    webbrowser.open(url=Url_Place)
    location = location.raw['address']
    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}
    current_loca = geocoder.ip('me')
    current_latlon = current_loca.latlng
    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)
    speak(target)
    speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")

def Notepad():
    speak("Tell Me .")
    speak("I Am Ready To Write .")
    writes = takecommand()
    time = datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","-") + "-note.txt"

    with open(filename,"w") as file:
        file.write(writes)
    path_1 = "C:\\Users\\Rahul Talukdar\\Desktop\\prog\\final\\" + str(filename)
    path_2 = "C:\\Users\\Rahul Talukdar\\Desktop\\prog\\final\\notepad\\" + str(filename)
    os.rename(path_1,path_2)
    os.startfile(path_2)

def CoronaVirus(Country):
    countries = str(Country).replace(" ","")
    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"
    result = requests.get(url)
    soups = BeautifulSoup(result.text,'lxml')
    corona = soups.find_all('div',class_ = 'maincounter-number')
    Data = []
    for case in corona:
        span = case.find('span')
        Data.append(span.string)
    cases= Data[0]
    Death=Data[1]
    recovored=Data[2]
    print(f"Cases : {cases}")
    speak(f"Cases : {cases}")
    print(f"Deaths : {Death}")
    speak(f"Deaths : {Death}")
    print(f"Recovered : {recovored}")
    speak(f"Recovered : {recovored}")




if __name__ == "__main__":
    while True:
       query = takecommand().lower()
       if 'you' in query:
         wishMe()
         battery = psutil.sensors_battery()
         percentage = battery.percent
         if(percentage<=20):
                speak(f"our system have only {percentage} percentage. please connect you charger")
         speak("If you want to ask me something then please activate my search mode .") 
         while True:
            query = takecommand().lower()
            if 'wikipedia' in query:
                speak('searching wikipedia.....')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak("according to wikipedia")
                speak(results)
            elif 'mode' in query:
                speak("just say activate search mode.")    
            elif 'search' in query and 'youtube' in query:
                query=query.replace("luna","")
                query=query.replace("search","")
                query=query.replace("in youtube","")
                query=query.replace("that","")
                webbrowser.open("https://www.youtube.com/results?search_query="+query)
                speak("Here you go sir.")
                speak("may i play some video for you?")
                yt2=takecommand().lower()
                if "yes" in yt2:
                    pywhatkit.playonyt(query)
                    speak("I guess it will help you.")
                    speak("sir, do you want to download this video")
                    la=takecommand().lower()    
                    if "yes" in la:
                        DownloadYoutube()
            elif 'whatsapp' in query:
                os.startfile("C:\\Users\\Rahul Talukdar\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
                whatsappauto()
            elif 'whatsapp chat' in query:
                name=takecommand().lower()
                Whatsappchat(name)
                whatsappauto()    
            elif 'whatsappcall' in query:
                speak("whome to call?")
                name=takecommand().lower()
                WhatsappCall(name)
            elif 'whatsapp message' in query:
                speak("whome to message?")
                name=takecommand().lower()
                WhatsappMsg(name) 
            elif 'whatsapp videocall' in query:
                speak("whome to call?")
                name=takecommand().lower()
                WhatsappVCall(name) 
            elif 'where is' in query:
                query=query.replace("where is ","")
                GoogleMaps(query)                       
            elif 'youtube' in query:
                webbrowser.open("https://www.youtube.com/")
                speak("Do you want to search anything in youtube?")
                query=takecommand().lower()
                if 'yes' in query:
                    speak("What do you want to search.")
                    yt=takecommand().lower()
                    yt=yt.replace("luna","")
                    yt=yt.replace("search","")
                    speak("okay, let me try.")
                    webbrowser.open("https://www.youtube.com/results?search_query="+yt)
                    time.sleep(3)
                    speak("Here you go sir.")
                    speak("may i play some video for you?")
                    yt2=takecommand().lower()
                    if "yes" in yt2 or "play" in yt2:
                        pywhatkit.playonyt(yt)
                        speak("I guess it will help you.")
                        speak("sir, do you want to download this video")
                        la=takecommand().lower()    
                        if "yes" in la:
                            DownloadYoutube()
                    elif "no" in yt2:
                        speak("would you like to handle it on your own?")
                        lt=takecommand().lower()
                        if 'no' in lt:
                           YouTubeAuto()
                        else:
                           pass
                elif 'no' in query:
                    speak("okay sir")  
                    speak("would you like to handle it on your own?")
                    lt=takecommand().lower()
                    if 'no' in lt:
                       YouTubeAuto()
                    else:
                       pass      
            elif 'break' in query or 'not now' in query:
                speak("okay sir.")
                time.sleep(30)
                speak("what about now?")
            
            elif 'open google' in query:
                speak("opening google.")
                webbrowser.open("https://www.google.com/")
                ChromeAuto()
            elif 'note' in query:
                Notepad()
            elif 'play music' in query:
                # speak("playing music ")
                # music_dir = 'D:\\songs'
                # songs = os.listdir(music_dir)
                #  print (songs)
                # os.startfile(os.path.join(music_dir, songs[1]))
                speak("where shall i play music for you spotify or in youtube")
                kj=takecommand().lower()
                if 'play' in kj:
                    speak("say the name!")
                    kj=takecommand().lower()
                    if 'wish' in kj:
                        speak("okay, Let me try")
                        os.startfile("C:\\Users\\Rahul Talukdar\\AppData\\Roaming\\Spotify\\Spotify.exe")
                        time.sleep(10)
                        press_and_release("Ctrl + L")
                        time.sleep(3)
                        write("sondhey namar agey")
                        time.sleep(5)
                        click(x=899, y=276)
                        click(x=1791, y=18)
                        speak("okay sir, Enjoy the music")
                        speak("I'm going to sleep")
                        time.sleep(40)
                    else:
                        os.startfile("C:\\Users\\Rahul Talukdar\\AppData\\Roaming\\Spotify\\Spotify.exe")
                        time.sleep(10)
                        press_and_release("Ctrl + L")
                        time.sleep(3)
                        write(kj)
                        time.sleep(5)
                        click(x=899, y=276)
                        click(x=1791, y=18)  

            elif 'battery' in query or 'power' in query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                if(percentage<=20):
                     speak(f"our system have only {percentage} percentage. please connect you charger")
                else:
                     speak(f"sir our system have {percentage} percent battery.")    
            elif 'listen' in query:
                speak("Yes!")    
            elif 'search' in query:
                speak("Yes sir, activating search mode")
                speak("search mode activated")
                while TRUE:
                    query = takecommand().lower()
                    if "deactivate" in query:
                        speak("search mode deactivated")
                        break
                    else:    
                        if "jarvis" in query:
                           query="J.A.R.V.I.S"
                        elif "tony stark" in query:
                            query="Tony Stark(Marvel Cinematic Universe)"     
                        GoogleSearch(query)
            elif "joke" in query:
                joke=pyjokes.get_joke()
                print(joke)
                speak(joke)           
            elif "where i am" in query or "where we are" in query:
                speak("wait sir, let me check !")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data=geo_requests.json()
                    city=geo_data['city']
                    country=geo_data['country']
                    speak(f"Sir i am not sure , but i think we are in {city} city of {country} country .")
                    op = f"https://www.google.com/maps/place/{city}"
                    webbrowser.open(op)
                except Exception as e:
                    speak("sorry sir,Due to network issue i am not able to find where we are .")
                    pass
            elif "shut down" in query:
                os.system("shutdown /s /t 5")
            elif "restart" in query:
                os.system("shutdown /r /t 5")     
            elif "switch the window" in query:
                press_and_release('Alt + Tab')   
            elif "picture" in query:
                speak("from which rover you want to see the picture . There are 4 rovers   Sojourner, Spirit and opportunity, Curiosity, and Perseverance. ") 
                name=takecommand().lower()
                speak("tell me the date you want to get the picture. Please tell me in the order of year month day.")
                date=takecommand().lower()
                # date = date.replace(" and ","-")
                # date = date.replace("and","-")
                # date = date.replace(" ","")
                # # data=DateConverter(date)
                # print(date)
                MarsImage()
            elif "space picture" in query:
                speak("please tell me the date in the order of year month day")
                date=takecommand().lower()
                date = date.replace(" and ","-")
                date = date.replace("and","-")
                date = date.replace(" ","")
                # data=DateConverter(date)
                NasaNews(date)
            elif "asteroid" in query:
                speak("by any chance ,Are you doubting in my abilities? ")
                speak("just tell me from which date you want to know ")
                date=takecommand().lower()
                # date = date.replace(" and ","-")
                # date = date.replace("and","-")
                # date = date.replace(" ","")
                # print(date)
                # data=DateConverter(date)
                speak("okay")
                speak("upto which date")
                date2=takecommand().lower()
                # date2 = date2.replace(" and ","-")
                # date2 = date2.replace("and","-")
                # date2 = date2.replace(" ","")
                # data2=DateConverter(date) 
                # print(date2)
                Astro('2022-07-03','2022-07-07')
            elif "covid" in query:
                speak("for which country you want to covid update")
                lm=takecommand().lower()
                CoronaVirus(lm)    
            elif "stars" in query:
                speak("about which star you want to know ?")
                star=takecommand().lower()
                solarbodies(star)
            elif "translate" in query:
                speak("tell me the line")
                line=takecommandinhindi()
                translate=Translator()
                result=translate.translate(line)
                speak(f"The translation for this line will be{result}")        
            elif "news" in query:
                speak("please wait")
                news()    
            elif "ip address" in query:
                ipAdd = requests.get('https://api.ipify.org').text
                speak(f"Your ip address is {ipAdd}") 
            elif 'home screen' in query:
               press_and_release('windows + d')
            elif 'minimize all' in query:
               press_and_release('windows + m')
            elif 'minimize' in query:
               press_and_release('Windows + Up Arrow')
               time.sleep(2)
               click(x=1791, y=18)  
            elif 'show start' in query:
               press('windows')
            elif 'check for' in query:
               speak("yes there are 6 messages in insta and 3 in Fb , shall i show you?")
               sc=takecommand().lower()
               if 'no' in sc:
                 speak("okay sir")
            elif 'open setting' in query:
               press_and_release('windows + i')
            elif 'open search' in query:
               press_and_release('windows + s')
            elif 'screen shot' in query:
               press_and_release('windows + SHIFT + s')
            elif 'restore windows' in  query:
               press_and_release('Windows + Shift + M')     
            elif "instagram profile " in query or "profile on instagram" in query:
                speak("sir please enter the user name correctly")
                name=input("Enter the user name here")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profile of {name}")       
                time.sleep(5)
                speak("sir would you like to download profile picture of this account")
                condition = takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name,profile_pic_only=True)
                    speak("i am done sir, profile picture is saved in our main folder. Now i am ready for next command")
                else:
                    pass
            elif "take screenshot" in query or "take one screenshot" in query:
                speak("sir , please tell me the name for this screenshot file")
                name = takecommand().lower()
                speak("please sir hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img=pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is saved in our main folder.")
            elif 'hide' in query:
                os.chdir('C:\\Users\\Rahul Talukdar\\Desktop\\secret')
                for file in os.listdir():
                    # print(file)
                    os.system(f'attrib +h /s "C:\\Users\\Rahul Talukdar\\Desktop\\secret\\{file}"') 
                speak("sir, all the files in our secret folder are now hidden .")
            elif 'my instagram account' in query: 
                   webbrowser.open(f"www.instagram.com/rahultalukdar33714")
                   speak("It looks really nice sir.")
                   speak("would you like to handle chrome on your own?")
                   lt=takecommand().lower()
                   if 'no' in lt:
                       ChromeAuto()
                   else:
                       pass   
            elif 'visible' in query:
                os.chdir('C:\\Users\\Rahul Talukdar\\Desktop\\secret')
                for file in os.listdir():
                    # print(file)
                    os.system(f'attrib -h /s "C:\\Users\\Rahul Talukdar\\Desktop\\secret\\{file}"')
                speak("sir, all the files are now visible to everyone. I wish you are taking this decision in your peace.")  
            elif 'query' in query or 'can' in query or 'problem' in query:
                speak("tell me your query. Please let me know when you are done with your queries. You are requested to speak a little bit slowly.")
                # know=takecommand().lower()
                # if 'calculate' in know or 'calculation' in know:
                #       speak("ok , now tell me you problem , i am opening my calculator")
                time.sleep(3)
                while True:
                   know2=takecommand().lower()
                   if "done" in know2:
                        speak("okay sir ")
                        break
                   else:
                         ser=know2.replace("plus","+")
                         ser=know2.replace("minus","-")
                         ser=know2.replace("into","*")
                         ser=know2.replace("multiplied by","*")
                         ser=know2.replace("divided by","/")
                         ser=know2.replace("by","/")
                         ser=know2.replace("bracket","(")
                         ser=know2.replace("bracket close",")")
                         ser=know2.replace("first bracket","(")
                         ser=know2.replace("first bracket close",")")
                         ser=know2.replace("second bracket ","{")
                         ser=know2.replace("second bracket close","}")
                         ser=know2.replace("third bracket ","[")
                         ser=know2.replace("third bracket close","]")
                         ser=know2.replace("open ","")
                         ser=know2.replace("jarvee ","")
                         #   ser=know2.replace("integral of ","∫")
                         ser=know2.replace("integration of ","∫")
                         ser=know2.replace("integral of ","∫")
                         ser=know2.replace("differentiation","differential")
                         ser=know2.replace("dot",".")
                         ser=know2.replace("to the power","^")
                         ser=know2.replace("square","^2")
                         ser=know2.replace("cube","^3")
                         ser=know2.replace("what will be","")
                         ser=know2.replace("ddx","differential")
                         ser=know2.replace("and"," ")
                         wolFrame(ser)
            elif 'volume up' in query:
                pyautogui.press("volumeup")
            elif 'volume down' in query:
                pyautogui.press("volumedown")
            elif 'luna' in query:
                speak("yes boss! I am here for you.")     
            elif 'mute' in query:
                pyautogui.press("volumemute")                  
            elif 'internet speed' in query:
                st=speedtest.Speedtest()
                dl=st.download()
                up=st.upload()
                speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
            elif 'set alarm' in query:
                speak(" Would you like to give me the time through speaking or by typing.")
                kh=takecommand().lower()
                if "speaking" in kh:
                    speak("tell me the time to set the alarm. For example, set alarm at 5 and 30 am")
                    tt=takecommand().lower()
                    tt=tt.replace("set alarm at ","")
                    tt=tt.replace(".","")
                    tt=tt.replace(" and ",":")
                    tt=tt.replace(" ","")
                    tt=input("enter the time :")
                elif "typing" in kh:
                   speak("yeah , i will suggest you to do the same as your microphone is not well.")   
                   tt=input("Enter the time :")
                   alarm_time=str(tt)
                # print(tt)
                speak("Alarm time is set")
                while True:
                    search = "temperature in my location"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    sta = data.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
                    data = sta.split('\n')
                    Time = data[0]
                    t=str(Time)
                    s=t.split()
                    T=s[1]
                    m=s[2]
                    current_time=f'{T} {m}'
                    # print(current_time)
                    if (current_time==alarm_time):
                        
                        # playsound("C:\\Users\\Rahul Talukdar\\Desktop\\alarm\\Avengers-Theme-Remix.mp3")
                        music_dir = "C:\\Users\\Rahul Talukdar\\Desktop\\alarm"
                        songs = os.listdir(music_dir)
                        os.startfile(os.path.join(music_dir, songs[0]))
                        gh=takecommand().lower()
                        if 'stop' in gh:
                            os.system("taskkill /f /im Music.UI.exe")
                            speak("Wake up sir , it's time to work. ")
                            break
                    elif (current_time>alarm_time):
                        break    
                
            # elif 'whatsapp' in query:
            #     speak("Tell me the number please!")
            #     num=takecommand().lower()
            #     speak("what do you want to say")
            #     msg=takecommand().lower()
            #     pywhatkit.sendwhatmsg(num,msg,datetime.datetime.now().hour,datetime.datetime.now().minute+1)
            #     speak("i have sent in your whatsapp.")
            elif 'play a song on youtube' in query:
                speak("Which song do you want to listen ?")
                sn=takecommand().lower()
                pywhatkit.playonyt(sn)  
                ChromeAuto() 
            elif 'open camera' in query:
                speak("hold a second. Openning camera.")
                cap=cv2.VideoCapture(0)
                cv2.namedWindow("test")
                img_count=0
                while True:
                    ret,frame=cap.read()
                    if not ret:
                        speak("Failed to grab frame!")
                        print("Failed to grab frame!")
                        break
                    cv2.imshow("test",frame)
                    time.sleep(10)
                    com=takecommand().lower()
                    if "click" in com:
                        speak("say cheeeeeese!")
                        img_name= f"opencv_frame_{img_count}"
                        cv2.imwrite(img_name,img)
                        speak("okay,your picture is taken")
                        img_count+=1
                    elif "close" in com:
                        speak("closing camera.")
                        break    
                cap.release()
                cv2.destroyAllWindows()              
            elif 'the time' in query:
                # strTime = datetime.datetime.now()("%f:%f:%s")
                speak(f"sir , the time is {T}{m}")
            elif 'open spotify' in query:
                codepath = "C:\\Users\\Rahul Talukdar\\AppData\\Roaming\\Spotify\\Spotify.exe"
                os.startfile(codepath)
            elif 'weather' in query:
                speak(f"its currently {sky} outside , sir!")
            elif 'temperature' in query:
                speak(f"its currently {temp} outside , sir!")
            # elif 'how are you' in query:
            #     speak("I am fine ! what about you?")
            # elif 'thank you' in query:
            #     speak("it's my pleasure sir.")
            elif 'message' in query:
                account_sid = 'ACa76b6d88fe570c855ebd60f539958deb'
                auth_token = 'fcffb63d4a06a8d0d48766cc0679892c'
                speak("Tell me the number and remember the number should be twilio verified.")
                num=takecommand().lower()
                speak("Tell what should i send ?")
                msg=takecommand().lower()
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                         body=msg,
                         from_ =  '+12097790632',
                         to = num
                     )
                print(message.sid)
            elif 'call' in query:
                account_sid = 'ACa76b6d88fe570c855ebd60f539958deb'
                auth_token = 'fcffb63d4a06a8d0d48766cc0679892c'
                speak("Tell me the number and remember the number should be twilio verified.")
                num=takecommand().lower()
                speak("Tell what should i say?")
                msg=takecommand().lower()
                client = Client(account_sid, auth_token)

                message = client.calls \
                    .create(
                         twiml=f'<Response><Say>{msg}</Response></Say>',
                         from_ =  '+12097790632',
                         to = num
                     )

                print(message.sid)        
            elif 'is my' in query:
                speak("That's great ! ")
                if 'father' in query:
                    speak("Hi sir , this is Luna ,glad to meet you.")
                elif 'mother' in query:
                    speak("Hi mam , this is Luna ,glad to meet you.")
            elif 'you know' in query:
                speak("obviously ! You know ? alexa ,siri , we all are best friends and jarvis is a crush for all of us.  ")  
            elif 'you be my' in query:
                speak("Fuck  off !")  
            elif 'love' in query:
                speak("I love you three thousand , but as a friend . ")     
            elif 'introduce' in query:
            #         speak("why?")
            # elif 'video' in query:        
                    print("Allow me to introduce myself. I am Jarvee , made by Rahul Talukdar.")
                    speak("Allow me to introduce myself , i am Luna , made by Rahul Talukdar. A virtual artificial intelligence and , i'm here, to assist you with a variety of tasks as best i can , 24 hours a day, seven days a week ,importing all preferences from home interface.")  
            elif 'close' in query:
                press_and_release('Alt + F4') 
                break
            elif 'restore' in query:
                press_and_release('Windows + Down Arrow') 
            elif 'maximize' in query:
                press_and_release('Windows + Up Arrow')
            elif 'minimize' in query:
                press_and_release('Windows + Up Arrow')
                time.sleep(2)
                click(x=1791, y=18) 
            elif 'minimize all' in query:
                press_and_release('Windows + M')
            elif 'go to the taskbar' in query:
                press_and_release('Windows + T')
            elif 'no' in query or 'go ahead' in query:
                press('Right Arrow')
            elif 'tap' in query:
                click(x=1522, y=476)
            elif 'left' in query:
                press('Left Arrow')
            elif 'up' in query:
                press('Up Arrow')
            elif 'down' in query:
                press('Down Arrow')                      
            # elif 'fine' in query:
            #     speak("that's great to hear from you.")        
            elif 'go to sleep' in query:
                 print("okay sir , wake me up when you want.")
                 hour = int(datetime.datetime.now().hour)
                 if hour >= 21:
                    speak("okay Good night sir, wake me up when you want.")
                 else:
                    speak("okay sir , wake me up when you want.")
                 quit()
            else:
                speak(ChatterBot(query))     


# elif "sleep" in query:
#                 os.system("rundl32.exe powrprof.dll,SetSuspendState 0,1,0")

# ACa76b6d88fe570c855ebd60f539958deb---->acc sid
# fcffb63d4a06a8d0d48766cc0679892c--->auth token
# +12097790632--->twilo phone number               