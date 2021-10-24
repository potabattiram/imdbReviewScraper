import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

response = requests.get(url)
html = BeautifulSoup(response.content,features="html.parser")

def dataExtracter():
    names = []
    ratings = []
    for i in range(1,10):
        names.append(html.findAll('table')[0].findAll('tr')[i]('td')[1].a.string)
        ratings.append(html.findAll('table')[0].findAll('tr')[i]('td')[2].strong.string)

    data = []
    for i in range(len(names)):
        data.append(names[i] + " " + ratings[i])
    return data
   
data = dataExtracter()
print(data)
    