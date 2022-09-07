import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.daraz.com.bd/smartphones/')
soup = BeautifulSoup(source.text, 'html.parser')

# print(soup.prettify())

# print(soup.p['class'])
# print(soup.p)
# print(soup.p.text)
# print(soup.p.get_text)

# print(soup.find_all("a"))
# for link in soup.find_all('a'):
#     print(link.get('href').split())

# dd = soup.find('div', id= "webim-container")
#     # print(tag.name)
# print(dd.getText)





# mobile_div = soup.select('.info--ifj7U > div')
mobile_div = soup.find('div', class_='inner--SODwy')
# print(len(mobile_div))
print(mobile_div)
for m in mobile_div:
    print(m.text.split())

