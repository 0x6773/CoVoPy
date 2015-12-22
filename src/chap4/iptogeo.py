#! /usr/bin/python2

import pygeoip
import optparse

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    print 'Details for %s' % tgt
    for key in rec.keys():
        print '%s : %s' %(key, rec[key])

def main():
    parser = optparse.OptionParser('usage %prog -i <IP Addr>')
    parser.add_option('-i', dest = 'ipAddr', type = 'string', help = 'specify IP Address')
    (options, args) = parser.parse_args()
    ipAddr = options.ipAddr
    if ipAddr == None:
        print parser.usage
        exit(0)
    else:
        print printRecord(ipAddr)

if __name__ == '__main__':
    main()
