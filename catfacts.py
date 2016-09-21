#!/usr/bin/env python

import getopt
import sys
import requests
import json

def get_cat_facts(num=1):
    facts = []
    r = requests.get(r'http://catfacts-api.appspot.com/api/facts?number={}'.format(num))
    js = json.loads(r.text)
    for f in js['facts']:
        facts.append(f)
    return facts

if __name__ == '__main__':
    num = 1
    opts, args = getopt.getopt(sys.argv[1:], 'n:')
    for o, a in opts:
        if o == '-n':
            num = a
    for f in get_cat_facts(num):
        print f
