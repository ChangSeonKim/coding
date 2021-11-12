from os import WIFCONTINUED
from bs4 import BeautifulSoup as BS
import requests as req
url = "https://comic.naver.com/webtoon/list?titleId=335885"
res = req.get(url)

soup = BS(res.text, "html.parser")


#tds = soup.select("table.type_5 tr td:nth-child(4) a")

trs = soup.select("table.viewList tr")


data_list=[]
for tr in trs:
    temp = []
    if len(tr.select("td.title")) == 0:
        continue
    data1=tr.select("td.title")[0].get_text(strip=True)
    
    

    data2=tr.select("div.rating_type>strong")[0].get_text(strip=True)
   
    data3=tr.select("td.num")[0].get_text(strip=True)
    

    #temp=td.get_text(strip=True)
    temp.append(data1)
    temp.append(data2)
    temp.append(data3)
    print(temp)
    data_list.append(temp)


