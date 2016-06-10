# -*- coding: UTF-8 -*-

import nltk

# Primeira execução: baixa os dados utilizados pela biblioteca
# nltk.download()

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

print pos_tagged_tokens
