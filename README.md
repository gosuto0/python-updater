# python-updater

## Overview
Simple updater for python

## Requirement
- Python
- requirements.txt

## Usage

Step1. Creation of json in pastebin<br>
1. Paste the version of the main unit and download link for main.exe in 1<br>
2. Paste the download link for updater.exe in 2<br>
```
1 {"ver": "0.0.1", "link": "https://anonfiles.com/MAINPROGRAM"}
2 {"link": "https://anonfiles.com/UPDATERPROGRAM"}
```

Step2. Update main.py and registry.py and updater.py
```
main.py
Update "#Programname" in line 23 to Your program name
Update "#pastebin#1" in line 32 to url of Step1. 1
Update "#pastebin#2" in line 33 to url of Step1. 2

registry.py
Update "#Programname" in line 6 to Your program name

file.py
Update "#Programname" in line 9 to Your program name

updater.py
Update "pastebin#1" in line 12 to url of step1. 1
Update "#Programname" in line 13 to Your program name
```

Step3. Pyinstaller<br>
Use pyinstaller to convert to exe
```
"pyinstaller --onefile --noconsole --icon=ICON.ico main.py"
"pyinstaller --onefile --noconsole --icon=ICON.ico updater.py"
```

Step4. Upload file<br>
Upload the exe-ized file to anonfile.<br>
Paste in the link in the json<br>

Step5. Updating<br>
When you want to update, rewrite self.ver in main.py and update pastebin#1 ver and link.<br>
Note: Please make sure that the ver of pastebin#1 is fine.<br>
