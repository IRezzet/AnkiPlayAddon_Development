import subprocess
import time
import psutil

''''counter = 0
while True:
    if counter >= 10:
        print("so viele minuten sind schon vergangen: %d", counter/60)
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


while True:
    print(checkIfProcessRunning('VCMI_launcher.exe'))'''

