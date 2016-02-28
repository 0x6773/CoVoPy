#! /usr/bin/python2

from anonbrowser import *
from BeautifulSoup import BeautifulSoup
import optparse

def printLinks(url):
    ab = anonBrowser()
    ab.anonymize()
    page = ab.open(url)
    html = page.read()
    try:
        print '[ + ] Printing links from BeautifulSoup'
        soup = BeautifulSoup(html)
        links = soup.findAll(name = 'a')
        for link in links:
            if link.has_key('href'):
                print link['href']
    except:
        pass

def main():
    parser = optparse.OptionParser('usage %prog -u <target url>')
    parser.add_option('-u', dest = 'tgtURL', type = 'string', help = 'specify target url')
    (options, args) = parser.parse_args()
    url = options.tgtURL
    if url == None:
        print parser.usage
        exit(0)
    else:
        printLinks(url)

if __name__ == '__main__':
    main()
