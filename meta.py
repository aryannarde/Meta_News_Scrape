import requests as rq
from bs4 import BeautifulSoup 
import pandas as pd


Metaurl = 'https://www.ft.com/stream/7e37c19e-8fa3-439f-a870-b33f0520bcc0'

MetaHeder = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

MetaResp = rq.get(url=Metaurl,headers=MetaHeder)

MetaSoup = BeautifulSoup(MetaResp.content,'html.parser')

Meta_news = MetaSoup.find_all('li',attrs={'class':'o-teaser-collection__item o-grid-row'})


    
News_data = [news.text for news in Meta_news ]
print(News_data)