#! /usr/bin/python2

import pexpect
from pexpect.pxssh import pxssh

botNet = []

class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception, e:
            print e
            print '[ - ] Error Connecting'

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def botNetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print '[ * ] Output from : ' + client.host
        print '[ + ] ' + output + '\n'

def main():
    addClient('127.0.0.1', 'mnciitbhu', '<-any->')
    addClient('localhost', 'mnciitbhu', '<-any->')
    botNetCommand('uname -v')
    botNetCommand('cat /etc/issue')

if __name__ == '__main__':
    main()
