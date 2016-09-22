#!/usr/bin/env python

import time
import getopt
import sys
import requests
import json
from twilio.rest import TwilioRestClient

def get_catfacts(num):
    r = requests.get(r'http://catfacts-api.appspot.com/api/facts?number={}'
                     .format(num))
    js = json.loads(r.text)
    return js['facts']

def get_catfact():
    return get_catfacts(1)[0]

def send_catfact(sendNumber):
    accountSID  = 'ACc30733d805a9177d3a1ca1d6efbd57cf'
    authToken   = 'c1ce6009d370d6bd26932ac218a101b5'

    twilioCli   = TwilioRestClient(accountSID, authToken)
    fromNumber  = '+15412925954'

    header      = 'Sent from your Twilio Trial account - '
    fact        = get_catfact()

    while len(fact) > 140 - len(header):
        fact = get_catfact()

    print 'Sending catfact: ' + fact
    message = twilioCli.messages.create(body=fact, from_=fromNumber, to=sendNumber)

    while message.status not in ('delivered', 'received', 'failed', 'undelivered'):
        time.sleep(1)
        message = twilioCli.messages.get(message.sid)

    print message.status + ' @ ' + str(message.date_sent)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        opts, args = getopt.getopt(sys.argv[1:], 's:', 'send=')
        for o, a in opts:
            if o in ('-s', '--send'):
                send_catfact(a)
    else:
        print get_catfact()
