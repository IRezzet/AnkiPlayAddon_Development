import subprocess
import time
from aqt import mw
from aqt.qt import *
import psutil


def denyAccess():
    counter = 0
    while True:
        subprocess.call('TASKKILL /F /IM VCMI_launcher.exe')
        if counter >= 20:
            break
        time.sleep(1)
        counter += 1


def startGame(Path):
    subprocess.Popen(Path)


def CloseGame():
    subprocess.call('TASKKILL /F /IM VCMI_launcher.exe')


def runForXTime():
    counter = 0
    while True:
        if counter >= 1800:
            break
        time.sleep(1)
        counter += 1


def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def testFunction() -> None:
    counter = 0
    startGame('C:/Program Files (x86)/VCMI (branch develop)/VCMI_launcher.exe')
    while checkIfProcessRunning('VCMI_launcher.exe'):
        if counter >= 20:
            denyAccess()
            break
        time.sleep(1)
        counter += 1


action = QAction("Start Playing", mw)
qconnect(action.triggered, testFunction)
mw.form.menuTools.addAction(action)
