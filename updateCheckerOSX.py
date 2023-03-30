import requests
import time
import os
import sys
from datetime import datetime
from sys import platform

url = ""
system = ""
title = "New version for " + url
message = "A new version for " + url + " has been detected"

def notify(title, text):
            os.system("""
            osascript -e 'display notification "{}" with title "{}"'
            """.format(text, title))

if __name__ == "__main__":

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])     
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
    print(r.text)
    notify("New Version", "A new version for " + url + " has been detected")