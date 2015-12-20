#! /usr/bin/python2

import urllib2
import optparse
from os.path import basename
from urlparse import urlsplit
from bs4 import BeautifulSoup

def findImages(url):
    print '[ + ] Getting HTML of %s' % url
    urlContent = urllib2.urlopen(url).read()
    soup = BeautifulSoup(urlContent, 'lxml')
    print '[ + ] Finding images on %s' % url
    imgTags = soup.findAll('img')
    if len(imgTags) != 0:
        print '[ + ] Total image(s) found : %d' % len(imgTags)
    else:
        print '[ - ] No images found at %s' % url
    for imgTag in imgTags:
        yield imgTag

def downloadImage(imgTag):
    try:
        imgSrc = imgTag['src']
        imgOpen = urllib2.urlopen(imgSrc)
        imgInfo = imgOpen.info()
        imgSize = int(imgInfo.getheaders('Content-Length')[0]) / 1024
        imgFileName = basename(urlsplit(imgSrc)[2])
        print '[ + ] Image FileName : %s, Image Size : %d KB' % (imgFileName, imgSize)
        print '[ + ] Ready download ([Y]/N) : ',
        opt = raw_input()
        if opt == 'n' or opt == 'N':
            print '[ - ] Not Downloading!'
            return
        print '[ + ] Downloading image...'
        imgContent  = urllib2.urlopen(imgSrc).read()
        print '[ + ] Saving to %s' % imgFileName
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except Exception, e:
        print 'Exception occurred : %s' % str(e)
        return ''

def main():
    parser = optparse.OptionParser('usage %prog -u <URL>')
    parser.add_option('-u', dest = 'urlName', type = 'string', help = 'specify url')
    (options, args) = parser.parse_args()
    urlName = options.urlName
    if urlName == None:
        print parser.usage
        exit(0)
    for imgTag in findImages(urlName):
        downloadImage(imgTag)

if __name__ == '__main__':
    main()
