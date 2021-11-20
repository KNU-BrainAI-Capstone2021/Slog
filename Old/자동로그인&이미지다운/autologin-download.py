from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#인스타그램 로그인
driver = webdriver.Chrome('chromedriver 경로를 입력') #예시 'C:/Users/sam56/Desktop/인스타 이미지/chromedriver.exe'
url = 'https://www.instagram.com'
driver.get(url)
time.sleep(4)
email = '여기에 아이디 입력'
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)
password = '여기에 비밀번호 입력'
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()
time.sleep(5)
#검색어를 입력하여 해당 페이지로 이동
def insta_search(word):
    url = 'https://www.instagram.com/explore/tags/' + word
    return url 
tag = input('검색할 태그를 입력하세요 : ')
url = insta_search(tag)
driver.get(url)
time.sleep(3)

#드라이버의 페이지 소스를 html에 저장
html = driver.page_source
soup = BeautifulSoup(html,'lxml')

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
        with open(r'이미지가 저장될 파일명'+ tag + str(n)+ '.jpg','wb') as h: #예시 'C:/Users/sam56/Desktop/인스타 이미지/img/'
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)
    print()

