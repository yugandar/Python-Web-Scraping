#!/usr/bin/python3

import urllib3
from bs4 import BeautifulSoup
import csv

http = urllib3.PoolManager()
r = http.request('GET', 'https://hasjob.co/?t=fulltime&t=contract&t=intern&t=freelance&t=volunteer&t=partner')
soup = BeautifulSoup(r.data, 'lxml')
cards = soup.find_all('a', class_='stickie')
# print(cards)
csv_data = []
for card in cards:
    data = {}
    data['url'] = "http:{}".format(card.get('href'))
    d = [x for x in list(card.children) if x != '\n']
    data['location'] = d[0].string
    data['date'] = d[1].string
    data['title'] = d[2].string
    data['name'] = d[3].string
    csv_data.append(data)

keys = [ 'title', 'name', 'url', 'location', 'date']
with open('jobs.csv', 'w') as csv_file:
    dict_writer = csv.DictWriter(csv_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(csv_data)
