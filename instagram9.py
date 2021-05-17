# 인스타그램 셀레니움으로 크롤링
# instagram2.py + 엑셀에 저장
# 1. 각자가 쓴 인스타그램 게시글로 들어갈 수 있는 url 받기
# 2. 각 url로 들어가 그곳에서 아이디, 태그 or 글 뽑기
# 3. 뽑은 태그 or 글을 txt파일로 저장하기.
# 4. 뽑은 아이디로 각자의 프로필화면으로 들어가 프로필 다운받기.

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

f = open("instagrampost2.txt", "r")
for line in f:
    arr_href.append(line)

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


# 2. 각 url로 들어가 그곳에서 아이디, 태그 or 글 뽑기.
arr_profile = []                                                                                # 프로필 화면 주소들 담김.
arr_id = []                                                                                     # 아이디 담김.
arr_hash = []                                                                                   # 해시태그만 저장.
arr_content = []                                                                                # 내용만 저장
count = 0
for h in arr_href:
    url = arr_href[count]                                                                       # 게시글 주소 담겨있음.(200개 이상)
    driver.implicitly_wait(2)
    driver.get(url)

    # id부분 찾아서 아이디, 프로필주소 저장
    try:   
        href = driver.find_elements_by_xpath('//*[@class="e1e1d"]')                             # <div class="e1e1d"> <a href="/아이디/"> 형식.
        print("id 클래스 검색성공", len(href))
        print("id[%d]" % count)
    except:
        print("id 클래스 검색실패")
        continue

    try:
        href_profile = href[0].find_element_by_css_selector('a').get_attribute('href')          # 프로필주소 검색
        arr_profile.append(href_profile)
    
        id = href[0].find_element_by_css_selector('a').text                                     # 아이디 검색.
        arr_id.append(id)
        print("id : %s" %id)
    except:
        print("아이디, 프로필주소 검색 실패, none으로 초기화")
        arr_profile.append("none")
        arr_id.append("none")
        
    # 댓글부분 찾아서 태그, 내용 저장
    try:
        href = driver.find_elements_by_xpath('//*[@class="C4VMK"]')                         # <div class="C4VMK"> <a href="/아이디/"></a> <span>내용</span> </div>형식.
        print("댓글 클래스 검색성공", len(href))                                            # or 태그라면 <span> <a></a> <a></a> <a></a> </span> 형식으로 되어있음.
        print("hash[%d]" % count)
    except:
        print("댓글 클래스 검색실패")

    text = ''
    nottext = ''
    i=0
    for i in range(0,3):                                                                    # 댓글을 위에서부터 세개까지만 받아올 것.
        try:
            hashid = href[i].find_element_by_css_selector('a').text                         # 댓글의 아이디를 받음.
            print("hashid = %s, arr_id[count] = %s" %(hashid, arr_id[count]))               # 댓글아이디와 현재 게시글의 작성자 아이디를 비교
            
            if(hashid == arr_id[count]):                                                    # C4VMK 클래스는 모든 댓글을 받아오므로 본인의 아이디인것만 받음.(아이디가 같다면)
                try:
                    hashtext = href[i].find_element_by_css_selector('span').text            # 댓글이 그냥 텍스트 내용이라면 여기서 검출될 것.(각 댓글중 0번째와 1번째만 봄.)
                    if(hashtext[0] != "#"):                                                 # hashtext[i] 번째가 #으로 시작하지 않으면 그냥 내용인 것.
                        text += hashtext+"/"                                                # text = "너무너무~~ 텍스트로 쓰여진 내용/" 으로 저장될 것.
                    else:                                                                   # 해시태그라면
                        nottext += hashtext                                                 # nottext = "#좋음#좋은날~~~" 으로 저장될 것.
#                    print("현재 검출된 텍스트 : ", text.translate(non_bmp_map))
                except:                                                                     # 댓글이 태그라면 여기로 넘어올 것.(hashtext부분에서 예외처리되어서.)
                    print("태그입니다.")
                    try:
                        count2 = 0
                        for u in href:                                                      # 각 댓글별로
                            print(count2)
                            try:                                                            # 태그받아오기 시도
                                for j in range(1, 30):
                                    tag = u.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/li[2]/div/div/div/span/a[%d]'%j).text    # 클래스검색 -> 그밑의 태그검색
                                    print("태그 받아옴[%d] : %s" %(j, tag))
                                    if(hashtext[0] != "#"):          # 받아온 글이 태그가 아니라면
                                        text += hashtext
                                        #hashtag.append(tag)
                                    else:
                                        nottext += hashtext+"/"
                            except:
                                print("태그 다받았거나 태그가 아님")
                            count2 = count2 + 1
                            if(count2 == 1):
                                break
                    except:
                        print("태그검색 실패")

                        for tag in href2:    
                            hashtext = tag.find_element_by_css_selector('span').find_element_by_css_selector('a').text
                            nottext += hashtext+"/"                                        # 너무너무/#어쩌고
        except:     # 댓글이 두개 이상 없을때.
            print("댓글이 많이없음")
#            print("현재 검출된 텍스트 : ", arr_hash)
    arr_hash.append(nottext)
    arr_content.append(text)
    print("-------------------------")
    
    count += 1
    
print("=================================================================")
print("id 수 : %d, 프로필주소 수 : %d, 해시태그, 내용 수 : %d" %(len(arr_id), len(arr_profile), len(arr_hash)))
#print(arr_id)
#print("\n")
#print(arr_profile)
#print("\n")
#print(arr_content)
#print("\n")
#print(arr_hash)
'''
count3 = 0
for t in arr_hash:
    print("arr_hash[%d] = %s"%(count3, t.translate(non_bmp_map)))
    count3 += 1
'''

# 3. 각 리스트(arr_id, arr_hash)를 다 만들었으면, 그 리스트를 다시 처리해 txt파일에 저장해줌.
'''
f = open("instagram.txt", "w", encoding='utf-8')
s = ''
for i in range(0, len(arr_id)):
    s += arr_id[i]+"\t"                                                                 # 각 아이디, 내용은 탭으로 나누고
    s += arr_hash[i]+"\n"                                                               # 내용 들어가면 엔터로 다음줄로 넘겨줌.
#    print(s.translate(non_bmp_map))
f.write(s)

f.close()
'''


from openpyxl import Workbook
wb = Workbook()
ws1 = wb.active
ws1.title = "instagram"
ws1["A1"] = "GENDER"
ws1["B1"] = "ID"
ws1["C1"] = "CONTENT"
ws1["D1"] = "TAG"

# id 넣기
count = 2
for id in arr_id:
    ws1["B"+str(count)] = id
    count += 1

# CONTENT 넣기
count = 2
for content in arr_content:
    ws1["C"+str(count)] = content
    count += 1

# hashtag 넣기
count = 2
for hash in arr_hash:
    ws1["D"+str(count)] = hash
    count += 1

wb.save("instagramWithForm.xlsx")

driver.quit()

print("Saved!")
