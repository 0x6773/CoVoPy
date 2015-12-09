#! /usr/bin/python2

import urllib2
import optparse
from os.path import basename
from urlparse import urlsplit
from bs4 import BeautifulSoup

def findImages(url):
    print '[ + ] Finding images on ' + url
    urlContent = urllib2.urlopen(url).read()
    soup = BeautifulSoup(urlContent, 'lxml')
    imgTags = soup.findAll('img')
    for imgTag in imgTags:
        yield imgTag

def downloadImage(imgTag):
    try:
        print '[ + ] Downloading image...'
        imgSrc = imgTag['src']
        imgContent  = urllib2.urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        print '[ + ] Saving to ' + imgFileName
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except Exception, e:
        print 'Exception occurred ' + str(e)
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
