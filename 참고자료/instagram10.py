# 인스타그램 셀레니움으로 크롤링
# 게시글 주소만 저장하기(instagrampost.txt 없을때. or 새글 검색할때)
import requests
import urllib.request
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

# 검색어
search = '오늘의훈남'
# url
url = 'https://www.instagram.com/explore/tags/' + search + '/?h1=ko'

driver = webdriver.Chrome(executable_path="D:\\python_D\\chromedriver.exe")
driver.implicitly_wait(2)
driver.get(url)

# 1. 각자가 쓴 인스타그램 게시글로 들어갈 수 있는 url 받기.
body = driver.find_element_by_tag_name("body")

num_of_pagedowns = 30
i = 0
count = 0
arr_href = []   # 게시글 주소들 담김.

# 게시글이 파일로 저장되어있으면 그걸 arr_href 에 넣는다.
'''
f = open("instagrampost.txt", "r")
for line in f:
    arr_href.append(line)
'''
print("게시글 개수 : %d"%len(arr_href))
# 게시글이 파일로 저장되어있지 않으면 받아온다.
if(len(arr_href) < 10):                                                                         # 숫자는 아무상관없음. 그냥 파일에 게시글주소 몇개 들어있는지 보는 것.
    while i < num_of_pagedowns:                                                                 # 페이지 다운 50번 할 것. 50번 하면서 댓글 실시간으로 불러옴.
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        try:
            post = driver.find_elements_by_xpath('//*[@class="v1Nh3 kIKUG  _bz0w"]')            # <div class="v1Nh3 kIKUG  _bz0w"> <a href="/p/암호화된 주소/?tagged=오늘의훈남"> 형식.
            print("클래스 검색성공", len(post))
        except:
            print("클래스 검색실패")
            
        if(i % 5 == 0):                                                                         # 임의로 page_down 5번 했을때 받아오는 것으로 함.
            n = 0
            for u in post:                                                                      
                if(n < 9):
                    n += 1                                                                      # 최근사진부분에서 가져올것이므로 인기게시물 9개는 건너뜀.
                else:
                    href = u.find_element_by_css_selector('a').get_attribute('href')            # 클래스검색 -> 그밑의 태그검색
                    #href = post[0].find_element_by_css_selector('a').get_attribute('href') 이것과 같음.
                    
                    print("주소받아옴[%d] : %s" %(count, href))
                    arr_href.append(href)
                    count = count + 1
            print("첫주소 : %s"%href)
        i += 1
        if(count > 300):
            break

    print("arr_href 개수 : %d"%len(arr_href))
    arr_href = list(set(arr_href))  #중복제거
    print("중복제거 arr_href 개수 : %d"%len(arr_href))

    # 게시물 주소 저장
    f = open("instagrampost2.txt", "w", encoding='utf-8')
    s = ''
    for i in range(0, 200):
        s += arr_href[i]+"\n"   # 내용 들어가면 엔터로 다음줄로 넘겨줌.
    f.write(s)
    print("게시글 주소 저장됨")
    f.close()

driver.quit()

print("Saved!")
