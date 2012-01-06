import urllib2
import BeautifulSoup

request = urllib2.Request("http://www.icheckmovies.com/list/top+100+spiritually+significant+films/xadoc/")
response = urllib2.urlopen(request)
soup = BeautifulSoup.BeautifulSoup(response)
for a in soup.findAll('a'):
    print a[0]


