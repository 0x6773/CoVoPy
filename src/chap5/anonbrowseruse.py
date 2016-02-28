#! /usr/bin/python2

from anonbrowser import *

ab = anonBrowser(proxies = [], user_agents = [('User-agents', 'superSecretBrowser')])

for attempt in range(1, 5):
    ab.anonymize()
    print '[ * ] Fetching page'
    reponse = ab.open('http://kittenwar.com')
    for cookie in ab.cookie_jar:
        print cookie
