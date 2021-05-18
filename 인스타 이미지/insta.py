from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# https://www.instagram.com/explore/tags/%ED%8C%8C%EC%9D%B4%EC%8D%AC/?hl=ko

#url이 계속 달라지니 base를 만든다
baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input('검색할 태그를 입력하세요 : ')
url = baseUrl + quote_plus(plusUrl)#아스키코드 변환안되어있으니

# url이 올바로 나오는지 테스트 
# print(url)

driver = webdriver.Chrome(r'C:\Users\sam56\Desktop\인스타 이미지/chromedriver.exe')
driver.get(url)

time.sleep(3)

#드라이버의 페이지 소스를 html에 저장
html = driver.page_source
soup = BeautifulSoup(html)

#insta에 태그를 저장한다
insta = soup.select('.v1Nh3.kIKUG._bz0w')

#출력확인
#print(insta)

#첫번째것만 확인하고 싶으면print(insta[0])사용

#반복문 작성(여러개 갖고와야 함)
n=1
for i in insta :
    print('https://www.instagram.com'+i.a['href'])
    #변수
    imgUrl = i.select_one('.KL4Bh').img['src']#태그 전체 가져오고, img중 src만을 저장
    #저장
    with urlopen(imgUrl) as f:
        with open(r'C:\Users\sam56\Desktop\인스타 이미지/img/'+ plusUrl+str(n)+ '.jpg','wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)
    print()


