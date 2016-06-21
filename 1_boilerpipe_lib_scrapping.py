# -*- coding: UTF-8 -*-

from boilerpipe.extract import Extractor
from bs4 import BeautifulSoup
from urllib2 import urlopen

N=5
URL='http://sportv.globo.com/site/eventos/mundial-de-motovelocidade/noticia/2016/06/em-duelo-eletrizante-rossi-vence-marquez-salom-e-homenageado.html'

soup = BeautifulSoup(urlopen(URL).read(), "lxml")
lista = soup.find_all("li", "noticia-plantao")
for li in lista[:N]:
    url = li.find("a")
    extractor = Extractor(extractor='ArticleExtractor', url=url["href"])
    print extractor.getText().encode('utf-8')
    print '-------------'

extractor = Extractor(extractor='ArticleExtractor', url=URL)
print extractor.getText().encode('utf-8')
