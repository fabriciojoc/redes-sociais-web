# -*- coding: UTF-8 -*-

import os
import sys
import json
import feedparser
from bs4 import BeautifulSoup

FEED_URL = 'http://www.stf.jus.br/portal/rss/noticiaRss.asp?codigo=1'

fp = feedparser.parse(FEED_URL)

print "Fetched %s entries from '%s'" % (len(fp.entries[0].title), fp.feed.title)

blog_posts = []
for e in fp.entries:
    blog_posts.append({'title': e.title,
                       'published': e.published,
                       'description': BeautifulSoup(e.description, 'lxml').get_text(),
                       'link': e.link})

out_file = os.path.join('./', 'feed.json')

f = open(out_file, 'w')
f.write(json.dumps(blog_posts, indent=1, ensure_ascii=False).encode('utf8'))
f.close()

print 'Wrote output file to %s' % (f.name, )
