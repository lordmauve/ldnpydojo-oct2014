#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twython import Twython

APP_KEY = 'YOUR_APP_KEY'
APP_SECRET = 'YOUR_APP_SECRET'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)


def how_drunk():
    print "hi"

if __name__ == "__main__":
    how_drunk()
