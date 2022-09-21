from aqt import mw
from aqt.qt import *
import threading
import subprocess
import time
import playtimeaddon.test.DenyAccessThreading as DenyAccessThreading

accesscheck = 0
DenyAccessThread = threading.Thread(target=DenyAccessThreading.denyAccess(accesscheck, 'VCMI_launcher.exe'))
DenyAccessThread.start()


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


def testFunction() -> None:
    counter = 0
    startGame('C:/Program Files (x86)/VCMI (branch develop)/VCMI_launcher.exe')
    while DenyAccessThreading.checkIfProcessRunning('VCMI_launcher.exe'):
        if counter >= 5:
            globals()['accesscheck'] = 1
            break
        time.sleep(1)
        counter += 1


action = QAction("Start Playing", mw)
qconnect(action.triggered, testFunction)
mw.form.menuTools.addAction(action)
