import requests
import time
import os
import sys
import ctypes
import notify2
from datetime import datetime
from sys import platform

url = ""
system = ""
title = "New version for " + url
message = "A new version for " + url + " has been detected"

def notify(title, text):
    if system == "win32":
        ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)
    elif system == "osx":
        os.system("""
        osascript -e 'display notification "{}" with title "{}"'
        """.format(text, title))
    elif system =="linux" or system == "linux2":
        notify2.init('Notification App')
        n = notify2.Notification(title, message)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.show()

if __name__ == "__main__":
    if platform == "linux" or platform == "linux2":
        system = "linux"
    elif platform == "darwin":
        system = "osx"
    elif platform == "win32":
        system = "windows"
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