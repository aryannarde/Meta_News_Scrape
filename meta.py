import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

Metaurl = 'https://www.ft.com/stream/7e37c19e-8fa3-439f-a870-b33f0520bcc0'

MetaHeder = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

MetaResp = rq.get(url=Metaurl, headers=MetaHeder)
MetaSoup = BeautifulSoup(MetaResp.content, 'html.parser')

dates = []
headings = []
contents = []
images = []

DateNews = MetaSoup.select('div[class="o-teaser-collection o-teaser-collection--stream"] > ul > li')

for n in DateNews:
    date = n.select_one('div[class="stream-card__date"] > time')
    dates.append(date.attrs['datetime'] if date else None)
    
    heading = n.select_one('div[class="o-teaser__heading"] > a')
    headings.append(heading.text.strip() if heading else None)
    
    content = n.select_one('p[class="o-teaser__standfirst"] > a')
    contents.append(content.text.strip() if content else None)
    
    img = n.select_one('div[class="o-teaser__image-placeholder"] > img')
    images.append(img.attrs['data-src'] if img else None)


NewsData = {
    'Date': dates,
    'Heading': headings,
    'Content': contents,
    'Image': images
}


df = pd.DataFrame(NewsData)
df.to_csv('news.csv')


