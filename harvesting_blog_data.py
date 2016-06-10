import os
import sys
import json
import feedparser
from bs4 import BeautifulSoup

FEED_URL = 'http://g1.globo.com/dynamo/rss2.xml'

def cleanHtml(html):
    return BeautifulSoup(html, 'lxml').get_text()

fp = feedparser.parse(FEED_URL)

print "Fetched %s entries from '%s'" % (len(fp.entries[0].title), fp.feed.title)

blog_posts = []
for e in fp.entries:
    blog_posts.append({'title': e.title,
                       'published': e.published,
                       'summary': cleanHtml(e.summary),
                       'link': e.link})

out_file = os.path.join('./', 'feed.json')

f = open(out_file, 'w')
f.write(json.dumps(blog_posts, indent=1))
f.close()

print 'Wrote output file to %s' % (f.name, )