##! /usr/bin/python2
"""

For Windows Only

"""

from _winreg import *

def val2addr(val):
    addr = ''
    for ch in val:
        addr += '%02x ' % ord(ch)
    return addr.strip(' ').replace(' ', ':')[0:17]

def printNets():
    net = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = OpenKey(HKEY_LOCAL_MACHINE, net)
    print '\n[ * ] Networks you have Joined.'
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            netKey = OpenKey(key, str(guid))
            (n, addr, t) = EnumValue(netKey, 5)
            (n, name, t) =  EnumValue(netKey, 4)
            macAddr = val2addr(addr)
            netName = str(name)
            print '[ + ] ' + netName + ' ' + macAddr
            CloseKey(netKey)
        except:
            pass

def main():
    printNets()

if __name__ == '__main__':
    main()
