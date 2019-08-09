from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('https://www.ecwid.com/showcase')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
images1 = bs.find_all('img', {'src':re.compile('.png')})
for image in images:
    print(image['src']+'\n')

for i in images1:
    print(i['src']+'\n')
