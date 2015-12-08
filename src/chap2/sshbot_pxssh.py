#! /usr/bin/python2

import pexpect
from pexpect.pxssh import pxssh

def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before

def connect(host, user, password):
    try:
        s = pxssh()
        s.login(host, user, password)
        return s
    except Exception, e:
        print e
        print '[ - ] Error Connecting'
        exit(0)

s = connect('10.1.1.18', 'root', '<-any->')
send_command(s, 'ls')
