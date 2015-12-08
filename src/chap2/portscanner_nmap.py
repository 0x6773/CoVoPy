#! /usr/bin/python2

import optparse
from threading import Thread, Lock
import nmap

lock = Lock()

def printScr(msg):
    global lock
    lock.acquire()
    print msg
    lock.release()

def nmapScan(tgtHost, tgtPort, all):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, str(tgtPort))
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    if all:
        if state != 'closed':
            printScr('[ + ] %s tcp / %s %s' % (tgtHost, tgtPort, state))
        else:
            printScr('[ - ] %s tcp / %s %s' % (tgtHost, tgtPort, state))
    elif state != 'closed':
        printScr('[ + ] %s tcp / %s %s' % (tgtHost, tgtPort, state))

    #print '[ * ] ' + tgtHost + 'tcp/' + tgtPort + " " + state

def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host')
    parser.add_option('-p', dest = 'tgtPort', type = 'string', help = 'specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    if tgtHost == None:
        print parser.usage
        exit(0)

    elif tgtPort == None:
        for port in range(1, 100):
            t = Thread(target = nmapScan, args = (tgtHost, port, False))
            t.start()
            #nmapScan(tgtHost, port, True)
    else:
        nmapScan(tgtHost, tgtPort, True)

if __name__ == '__main__':
    main()
