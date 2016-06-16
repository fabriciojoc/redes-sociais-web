# -*- coding: UTF-8 -*-

import feedparser

FEED_URL = "http://www.stf.jus.br/portal/rss/noticiaRss.asp?codigo=1"

fp = feedparser.parse(FEED_URL)
for f in fp.entries:
    print "Título: ", f.title
    print "Publicado: ", f.published
    print "Resumo:", f.summary
    print "Descrição: ", f.description
    print '------'
