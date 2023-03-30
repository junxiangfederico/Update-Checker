import requests
import time
import os
import sys
import pip
import ctypes
from datetime import datetime
from sys import platform

url = ""
system = ""
title = "New version for " + url
message = "A new version for " + url + " has been detected"



def import_or_install(package):
    print('installing')
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])     

def notify(title, text):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)
   

if __name__ == "__main__":
    import_or_install('ctypes')
    import_or_install('requests')
    url = input("Enter the URL you want to check: ")
    try:
        r = requests.get(url, allow_redirects=True)
    except:
        r = requests.get("https://" + url, allow_redirects=True)
    previousHash = hash(r.text)
    while (1==1):
        try:
            r = requests.get(url, allow_redirects=True)
        except:
            r = requests.get("https://" + url, allow_redirects=True)
        if (previousHash == hash(r.text)):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            string = "No new update as of " + current_time + "\r"
            sys.stdout.write("\b%s" % string)
            time.sleep(5)
        else:
            break
    
    notify("New Version", "A new version for " + url + " has been detected")