#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twython import Twython

APP_KEY = 'RddQXpqEMdGcQRswT4FCfXmSy'
APP_SECRET = 'Szu8XP6R4NxjOGfeTrbszlq7NJreCZEd97ufcHPxkaTjLiHrj4'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

words = ['beer',]

def get_lats_longs():
    twitter.search_geo(
        query='London',
    )


def how_drunk():
    tweets = twitter.search(
        q='-RT',
        geocode='51,0,10mi',
        result_type='recent',
        count='5')

    for tweet in tweets['statuses']:
        print tweet

if __name__ == "__main__":
    how_drunk()
