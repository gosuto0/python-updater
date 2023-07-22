import winreg
import os

class winreg_manager:
    def __init__(self):
        self.programname = "#Programname"
        self.path = "Software\Microsoft\Windows\CurrentVersion\Run"
        self.main_path = os.path.expanduser('~')+f"\AppData\Local\Programs\{self.programname}.exe"
        if self.check_startup():
            self.write_startup()

    def check_startup(self):
        key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, self.path, access=winreg.KEY_READ)
        try:
            winreg.QueryValueEx(key, self.programname)
        except:
            self.write_startup()
        winreg.CloseKey(key)

    def write_startup(self):
        key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, self.path, access=winreg.KEY_WRITE)
        winreg.SetValueEx(key, self.programname, 0, winreg.REG_SZ, f'"{self.main_path}" --autostart')
        winreg.CloseKey(key)