import os
import sqlite3
import subprocess
import time
import webbrowser

import pyautogui
from engine.helper import extract_yt_term, remove_words
from engine.config import ASSISTANT_NAME
from engine.command import speak
import pywhatkit as kit
import re
from sqlite3 import Cursor
from pipes import quote

con=sqlite3.connect("jarvis.db")
cursor=con.cursor()
# from playsound import playsound
# import eel
# @eel.expose
# # playing assistant sound function
# def playAssistantSound():
#      music_dir="www\\assests\\audio\\start_sound.mp3"
#      playsound(music_dir)
def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"")
    query=query.replace("open","")
    query.lower()
    app_name=query.strip()
    if app_name!="":
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

def PlayYoutube(query):
    search_term=extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    #pattern=r'\play\s+(.*?)\s+on\s+youtube'
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None
def findContact(query):
    
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        jarvis_message = "staring video call with "+name

    # Encode the message for URL
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)