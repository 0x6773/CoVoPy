#! /usr/bin/python2

from anonbrowser import *
from BeautifulSoup import BeautifulSoup
import optparse, os

def mirrorImages(url, dir):
    ab = anonBrowser()
    ab.anonymize()
    html = ab.open(url)
    soup = BeautifulSoup(html)
    image_tags = soup.findAll('img')
    for image in image_tags:
        filename = image['src'].strip('http://')
        filename = os.path.join(dir, filename.replace('/', '_'))
        print '[ + ] Saving' + str(filename)
        data = ab.open(image['src']).read()
        ab.back()
        save = open(filename, 'wb')
        save.write(data)
        save.close()

def main():
    parser = optparse.OptionParser('usage %prog -u <target url> -d <destination directory>')
    parser.add_option('-u', dest = 'tgtURL', type = 'string', help = 'specify target url')
    parser.add_option('-d', dest = 'dir', type = 'string', help = 'specify destination directory')
    (options, args) = parser.parse_args()
    url = options.tgtURL
    dir = options.dir
    if url == None or dir == None:
        print parser.usage
        exit(0)
    else:
        try:
            mirrorImages(url, dir)
        except Exception, e:
            print '[ - ] Error Mirroring Images.'
            print '[ - ] ' + str(e)

if __name__ == '__main__':
    main()
