# -*- coding: UTF-8 -*-

import feedparser

FEED_URL = "http://g1.globo.com/dynamo/rss2.xml"

fp = feedparser.parse(FEED_URL)
# print fp['feed']
for f in fp.entries:
    # print f.summary_detal.value
    print "Título: ", f.title
    print "Publicado: ", f.published
    print "Resumo:", f.summary
    tags = ""
    for t in f.tags:
        tags += t.term + " "
    print "Tags: ", tags
    # print f.value
    print '------'
