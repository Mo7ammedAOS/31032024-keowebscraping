from bs4 import BeautifulSoup as Bs
import requests
import csv
import pandas as pd

url = 'https://www.keoic.com/people'
html_keo = requests.get(url).text
soup = Bs(html_keo,'html5lib')
departments = soup.find_all('h1',class_='font_0 wixui-rich-text__text')
# print(title)
keys = []
for section in departments:
    section_name = section.find('span',class_="wixui-rich-text__text").text
    keys.append(section_name)
managers = soup.find_all('div', class_='nZLWPi l2B6lS')
values = []
for index,manager in enumerate(managers) :
    all_mangers = manager.find_all('div',class_="dFFOyU")
    inner = []
    for person in all_mangers:
        item_p = person.div.text+'|'+person.p.text
        inner.append(item_p)
    values.append(inner)

print(keys)
print()
print()
print(values[0])