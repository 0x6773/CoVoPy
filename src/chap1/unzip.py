#! /usr/bin/python2

import zipfile
import optparse
from threading import Thread

found = False

def extractFile(zFile, password):
    global found
    try:
        zFile.extractall(pwd = password)
        print '[ + ] Found ' + password
        found = True
    except:
        print '[ - ] Not Found ' + password

def main():
    parser = optparse.OptionParser("usage %prog -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest = 'zname', type = 'string', help = 'specify zip file')
    parser.add_option('-d', dest = 'dname', type = 'string', help = 'specify dictionary file')
    (options, args) = parser.parse_args()
    if options.zname == None or options.dname == None:
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile:
        password = line.strip('\n')
        if not found:
            t = Thread(target = extractFile, args = (zFile, password))
            t.start()
            #extractFile
        else:
            exit(0)

if __name__ == '__main__':
    main()
