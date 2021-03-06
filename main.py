#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from twython import Twython
import re

APP_KEY = 'RddQXpqEMdGcQRswT4FCfXmSy'
APP_SECRET = 'Szu8XP6R4NxjOGfeTrbszlq7NJreCZEd97ufcHPxkaTjLiHrj4'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

with open('words.txt') as word_file:
    words = [word.strip() for word in word_file]
    query = " OR ".join(words)
    drunkeness_regex = re.compile(
        r'(^|\s|#)(%s)\b' % "|".join(words)
    )
    # print drunkeness_regex.pattern
    # import sys
    # sys.exit()

with open('cities.txt') as city_file:
    cities = {}
    for city in city_file:
        name, geocode = city.strip().split()
        cities[name] = geocode


def get_tweets(location):
    tweets = twitter.search(
        q='{} -RT'.format(query),
        geocode=location,
        result_type='recent',
        count='100'
    )
    return [t["text"] for t in tweets["statuses"]]


def get_drunkeness(tweet):
    return sum(1 for _ in drunkeness_regex.finditer(tweet))


def drunkeness_of_location(location):
    tweets = get_tweets(location)
    # print tweets
    return int(sum(get_drunkeness(t) for t in tweets) / len(tweets) * 100)


def how_drunk():
    tweets = twitter.search(
        q='-RT',
        geocode='51,0,10mi',
        result_type='recent',
        count='5')

    for tweet in tweets['statuses']:
        print tweet


def test_drunk():
    pass


if __name__ == "__main__":
    for city, geocode in cities.iteritems():
        print "{} is {}% drunk".format(city, drunkeness_of_location(geocode))
