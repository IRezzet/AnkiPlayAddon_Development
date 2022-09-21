import subprocess
import time
from tkinter import messagebox

period = input("How long does it stay open?\n")


def getConvertedLocaltime():
    t = time.localtime()
    currentHours = time.strftime("%H", t)
    currentMinutes = time.strftime("%M", t)
    currentSeconds = time.strftime("%S", t)
    seconds = (int(currentHours) * 60 * 60) + (int(currentMinutes) * 60) + int(currentSeconds)
    return seconds


def denyAccess(Game):
    while 1:
        subprocess.call('TASKKILL /F /IM VCMI_launcher.exe')


def startGame(Path):
    subprocess.Popen(Path)


def CloseGame():
    subprocess.call('TASKKILL /F /IM VCMI_launcher.exe.exe')


startGame('C:\Program Files (x86)\VCMI (branch develop)\VCMI_launcher.exe')
# time.sleep(int(period) - 2)
# messagebox.showinfo("Warning!", "The game will close in 2s")
time.sleep(int(period))
CloseGame()
print(getConvertedLocaltime())
