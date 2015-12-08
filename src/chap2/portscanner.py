#! /usr/bin/python2

import optparse
from threading import Thread, Lock
from socket import *

lock = Lock()

def printScr(msg):
    global lock
    lock.acquire()
    print msg
    lock.release()

def connScan(tgtHost, tgtPort, all):
    global lock
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        printScr('[ + ] %d/tcp open for %s' % (tgtPort, tgtHost))
        connSkt.close()
    except:
        if all:
            printScr('[ - ] %d/tcp close' % tgtPort)

def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host')
    parser.add_option('-p', dest = 'tgtPort', type = 'int', help = 'specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    setdefaulttimeout(2)
    if tgtHost == None:
        print parser.usage
        exit(0)
    elif tgtPort == None:
        for port in range(1, 2**13):
            t = Thread(target = connScan, args = (tgtHost, port, False))
            t.start()
            #connScan(tgtHost, port, True)
    else:
        connScan(tgtHost, tgtPort, True)
    """
    for x in (1, 254):
        t = Thread(target = connScan, args = ('10.3.31.' + str(x), 23, False))
        t.start();
    """
if __name__ == '__main__':
    main()
