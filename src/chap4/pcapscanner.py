#! /usr/bin/python2

import dpkt
import socket

def printPcap(pcap):
    st = set()
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            if not (src, dst) in st:
                print '[ + ] Src : ' + src + ' --> Dst : ' + dst
                st.add((src, dst))
        except:
            pass

def main():
    f = open('/home/mnciitbhu/ws/pychk.pcap')
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)

if __name__ == '__main__':
    main()
