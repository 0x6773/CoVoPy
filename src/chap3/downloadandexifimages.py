#! /usr/bin/python2

import urllib2
import optparse
from os.path import basename
from urlparse import urlsplit
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS

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
        imgType = imgInfo.getheaders('Content-Type')[0]
        imgFileName = basename(urlsplit(imgSrc)[2])
        print '[ + ] Image FileName : %s, Type : %s, Image Size : %d KB' % (imgFileName, imgType, imgSize)
        print '[ i ] Ready download ([Y]/N) : ',
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
        print '[ + ] Saved to %s' % imgFileName
        return imgFileName
    except Exception, e:
        print 'Exception occurred : %s' % str(e)

def testForExif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print '[ * ] %s contains GPS MetaData' % imgFileName
    except AttributeError, ae:
        print 'Exception occurred : %s' % str(ae)
    except Exception, e:
        print 'Exception occurred : %s' % str(e)


def main():
    parser = optparse.OptionParser('usage %prog -u <URL>')
    parser.add_option('-u', dest = 'urlName', type = 'string', help = 'specify url')
    (options, args) = parser.parse_args()
    urlName = options.urlName
    if urlName == None:
        print parser.usage
        exit(0)
    for imgTag in findImages(urlName):
        imgFileName = downloadImage(imgTag)
        if imgFileName:
            testForExif(imgFileName)

if __name__ == '__main__':
    main()
