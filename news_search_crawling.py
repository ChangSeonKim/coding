from bs4 import BeautifulSoup
import requests

# html 가져오기
query = input('입력하세요:')
url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={query}"



req = requests.get(url)


soup = BeautifulSoup(req.text, 'html.parser')

print('>>>')
# print("#'{}' 검색결과".format(query))
# print('>>>')
a_list = soup.find_all('a', {'class':'news_tit'})
#a_list = soup.select('a.news_tit')

for a in a_list :
    print("title: " , a.get('title'))
    print('link: ' , a.get('href'))
