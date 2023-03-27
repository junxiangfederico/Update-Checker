import requests
import time
import os
import sys
from datetime import datetime
import requests

import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
 

 
def sendMessage(message):
    phone = '+'
  
    # creating a telegram session and assigning
    # it to a variable client
    
    # get your api_id, api_hash, token
    # from telegram as described above
    api_id = ''
    api_hash = ''
    token = ''
    TOKEN = ""
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    print(requests.get(url).json())

def sendMessageTelegram():
    id = ''
    TOKEN = ""
    message = "Update arrived, check! "
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id}&text={message}"
    print(requests.get(url).json()) # this sends the message


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
def baseRun():

    url = input("Enter the URL you want to check: ")
    r = requests.get(url, allow_redirects=True)
    previousHash = hash(r.text)
    while (1==1):
        r = requests.get(url, allow_redirects=True)
        if (previousHash == hash(r.text)):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            string = "No new update as of " + current_time + "\r"
            sys.stdout.write("\b%s" % string)
            time.sleep(5)
        else:
            break
    
    notify("New Version", "A new version for " + url + " has been detected")
    print("Sending message on telegram")
    sendMessageTelegram()

if __name__ == "__main__":
    #sendMessage(message)
    baseRun()