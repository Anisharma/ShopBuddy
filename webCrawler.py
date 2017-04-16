import urllib2
from BeautifulSoup import BeautifulSoup
url = "http://compare.buyhatke.com"
page = urllib2.urlopen("http://compare.buyhatke.com/")
soup = BeautifulSoup(page)
pole = int(input())
for link in soup.findAll('a'):
		if pole ==1 and 'Coupons' in str(link.get('title')): print url+link.get('href')
		elif pole == 2 and 'best deals' in str(link.get('title')): print url+link.get('href')  
		elif pole == 3 and 'Grab this Deal' in str(link): print url+link.get('href')