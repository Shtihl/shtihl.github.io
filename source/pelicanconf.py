#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Shtihl'
SITENAME = 'something about anything'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = '../'
THEME = "template/pelican-simplegrey"
TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 20
SUMMARY_END_SUFFIX = '…'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True