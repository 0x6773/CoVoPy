#! /usr/bin/python2

import os
import sqlite3
import optparse

def printProfile(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("""SELECT fullname, skypename, city, country,
                 datetime(profile_timestamp, 'unixepoch') FROM Accounts;""")
    for row in c:
        print '[ * ] --- Found Account ---'
        print '[ + ] User : %s' % str(row[0])
        print '[ + ] Skype UserName : %s' % str(row[1])
        print '[ + ] Location : %s, %s' % (str(row[2]), str(row[3]))
        print '[ + ] Profile Data : %s' % str(row[4])










def main():
    parser = optparse.OptionParser('usage %prog -p <skype profile path>')
    parser.add_option('-p', dest = 'pathName', type = 'string', help = 'specify skype profile path')
    (options, args) = parser.parse_args()
    pathName = options.pathName
    if pathName == None:
        print parser.usage
        exit(0)

    elif os.path.isdir(pathName) == False:
        print '[ i ] Path does not Exists : %s' % pathName
        exit(0)
    else:
        skypeDB = os.path.join(pathName, 'main.db')
        if os.path.isfile(skypeDB):
            printProfile(skypeDB)
        else:
            print '[ i ] Skype DataBase does not Exists : %s' % skypeDB

if __name__ == '__main__':
	main()
