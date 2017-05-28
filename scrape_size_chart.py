from bs4 import BeautifulSoup
import urllib

html = urllib.urlopen('http://shop.nordstrom.com/s/19-cooper-strappy-sheath-dress/sizeAndFitInfo/4608234?tn=Sizeandfit_popup&origin=sizechart').read()
soup = BeautifulSoup(html)
print(soup.prettify())
