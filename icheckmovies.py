import urllib2
from BeautifulSoup import BeautifulSoup,BeautifulStoneSoup
import re

soup = BeautifulSoup(urllib2.urlopen('http://www.icheckmovies.com/list/top+100+spiritually+significant+films/').read(),convertEntities=BeautifulStoneSoup.HTML_ENTITIES)

#lista = soup.findAll('a',href=re.compile(r'movie'),text=True)
lista = soup.findAll('a')
#print(lista)
#print(len(lista))

a = set()
for tagA in lista:
    if '/movie/' in tagA['href']:
        #print tagA['href']
        a.add(tagA.string)
print 'size A: %d' % len(a) 

soup250 = BeautifulSoup(urllib2.urlopen('http://www.icheckmovies.com/list/top+250/').read(),convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
#list250 = soup250.findAll('a',href=re.compile(r'movie'),text=True)
list250 = soup250.findAll('a')

#print(list250)
#print(len(list250))

b = set()
for tagB in list250:
    if '/movie/' in tagB['href']:
        #print tagB['href']
        b.add(tagB.string)
print 'size B: %d' %len(b)

c = a.intersection(b)
#print(c)
for item in c:
    print item
print 'Total intersection: %d' % len(c) 

