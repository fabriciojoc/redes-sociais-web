# -*- coding: UTF-8 -*-

import json
import nltk

# Baixa os dados utilizados pela biblioteca
nltk.download('stopwords')

BLOG_DATA = "./feed.json"

blog_data = json.loads(open(BLOG_DATA).read())

# Stop words

stop_words = nltk.corpus.stopwords.words('portuguese') + [
    '.',
    ',',
    '--',
    '\'s',
    '?',
    ')',
    '(',
    ':',
    '\'',
    '\'re',
    '"',
    '-',
    '}',
    '{',
    u'—',
    '%'
    ]

for post in blog_data:
    sentences = nltk.tokenize.sent_tokenize(post['summary'])

    words = [w.lower() for sentence in sentences for w in
             nltk.tokenize.word_tokenize(sentence)]

    fdist = nltk.FreqDist(words)

    # Estatísticas

    num_words = sum([i[1] for i in fdist.items()])
    num_unique_words = len(fdist.keys())

    # Hapaxes: palavras que aparecem uma única vez

    num_hapaxes = len(fdist.hapaxes())

    top_10_words_without_stop_words = [w for w in fdist.items() if w[0]
                                    not in stop_words][:10]

    print 'Title: ',post['title']
    print 'Summary: ', post['summary']
    print '\tNum Sentences:'.ljust(25), len(sentences)
    print '\tNum Words:'.ljust(25), num_words
    print '\tNum Unique Words:'.ljust(25), num_unique_words
    print '\tNum Hapaxes:'.ljust(25), num_hapaxes
    print '\tTop 10 Most Frequent Words (without stop words):\n\t\t', \
            '\n\t\t'.join(['%s (%s)'
            % (w[0], w[1]) for w in top_10_words_without_stop_words])
    print
