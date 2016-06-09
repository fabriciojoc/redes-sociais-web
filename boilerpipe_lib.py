# -*- coding: UTF-8 -*-

from boilerpipe.extract import Extractor

URL='http://sportv.globo.com/site/eventos/mundial-de-motovelocidade/noticia/2016/06/em-duelo-eletrizante-rossi-vence-marquez-salom-e-homenageado.html'

extractor = Extractor(extractor='ArticleExtractor', url=URL)

print extractor.getText().encode('utf-8')
