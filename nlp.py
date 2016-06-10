# -*- coding: UTF-8 -*-

import nltk

# Baixa os dados utilizados pela biblioteca
nltk.download('punkt')
nltk.download('maxent_treebank_pos_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# EOS Detection

txt = "Mr. Green killed Colonel Mustard in the study with the \
       candlestick. Mr. Green is not a very nice fellow."

sentences = nltk.tokenize.sent_tokenize(txt)

# Tokenization

tokens = []
for s in sentences:
    tokens.append(nltk.tokenize.word_tokenize(s))

# POS Tagging

pos_tagged_tokens = []
for t in tokens:
    pos_tagged_tokens.append(nltk.pos_tag(t))

# Chunking

ne_chunk = []
for chunk in nltk.ne_chunk_sents(pos_tagged_tokens):
    ne_chunk.append(chunk)

for c in ne_chunk:
    print c
