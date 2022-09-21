import time
import subprocess
import psutil


def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def denyAccess(access_check, filePath):
    counter = 0
    if access_check == 1:
        while True:
            if checkIfProcessRunning(filePath):
                subprocess.call('TASKKILL /F /IM ' + filePath)
            if counter >= 20:
                counter -= counter
                break
            time.sleep(1)
            counter += 1
