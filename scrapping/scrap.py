from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.hepsiemlak.com/istanbul-avcilar-denizkoskler-satilik/daire/0-36934620'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll()
print(len(containers))

live:.cid.b9801c2473b40606:!--!
