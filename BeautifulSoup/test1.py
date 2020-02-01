import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://python123.io/ws/demo.html')
# print(r.text)
demo = r.text
soup = BeautifulSoup(demo,'html.parser')
# print(soup.a.parent.name)
# print(soup.a.name)
# print(soup.a.attrs)
# print(soup.a.attrs['class'])
# print(soup.a.string)
# print(soup.p.string)
# print(soup.b.string)
# print(soup.head.contents)
# print(soup.body.contents)
# print(soup.prettify())
# for link in soup.find_all('a'):
# #     print(link.get('href'))
# # print(soup.find_all('a'))
# # for tag in soup.find_all(True):
# #     print(tag.name)
# # for tag in soup.find_all(re.compile('b')):
# #     print(tag.name)
print(soup.find_all(string = re.compile('Basic')))