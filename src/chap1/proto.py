#! /usr/bin/python2

import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def main():
    portList = [21, 22, 23, 80, 110, 443]
    for x in range(1, 20):
        ip = '192.168.0.' + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            print "[ + ] For ip:port -> " + ip + " : " + str(port)  + " ",
            if banner:
                print banner
            else:
                print "None"

if __name__ == '__main__':
    main()
