# -*- coding: UTF-8 -*-

import nltk

# Primeira execução: baixa os dados utilizados pela biblioteca
# nltk.download()

txt = "Mr. Green killed Colonel Mustard in the study with the \
       candlestick. Mr. Green is not a very nice fellow."

sentences = nltk.tokenize.sent_tokenize(txt)

print sentences
