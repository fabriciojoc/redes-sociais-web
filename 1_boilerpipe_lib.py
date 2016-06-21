# -*- coding: UTF-8 -*-

from boilerpipe.extract import Extractor

URL='http://sportv.globo.com/site/eventos/mundial-de-motovelocidade/noticia/2016/06/em-duelo-eletrizante-rossi-vence-marquez-salom-e-homenageado.html'
# URL='http://grandepremio.uol.com.br/motogp/noticias/rossi-supera-largada-ruim-vence-duelo-com-marquez-e-chega-a-10-vitoria-na-catalunha-lorenzo-abandona'

extractor = Extractor(extractor='ArticleExtractor', url=URL)

print extractor.getText().encode('utf-8')
