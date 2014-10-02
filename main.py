#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twython import Twython

APP_KEY = 'RddQXpqEMdGcQRswT4FCfXmSy'
APP_SECRET = 'Szu8XP6R4NxjOGfeTrbszlq7NJreCZEd97ufcHPxkaTjLiHrj4'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)


def how_drunk():
    tweets = twitter.search(
        q='-RT',
        geocode='51,0,10mi',
        result_type='recent',
        count='100')

    for tweet in tweets['statuses']:
        print tweet['text']

if __name__ == "__main__":
    how_drunk()
