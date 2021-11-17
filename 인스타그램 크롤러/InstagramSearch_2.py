
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import shutil

driver = webdriver.Chrome(r'C:\Users\brass\Desktop\Insta\chromedriver.exe') #경로지정
url = 'https://www.instagram.com'
driver.get(url)
time.sleep(4)
email = '(ID)'
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)
password = '(Password)'
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
time.sleep(10)

#드라이버의 페이지 소스를 html에 저장
html = driver.page_source
soup = BeautifulSoup(html,'lxml')

imglist = []


for i in range(0, 20):

    insta = soup.select('.v1Nh3.kIKUG._bz0w')

    for i in insta:

        print('https://www.instagram.com'+ i.a['href'])
        imgUrl = i.select_one('.KL4Bh').img['src']
        imglist.append(imgUrl)
        imglist = list(set(imglist))
        html = driver.page_source
        soup = BeautifulSoup(html)
        insta = soup.select('.v1Nh3.kIKUG._bz0w')

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

n=0
#뒤의 숫자가 저장되는 이미지 갯수
for i in range(0, 200):
    # This is the image url.
    image_url = imglist[n]
    # Open the url image, set stream to True, this will return the stream content.
    resp = requests.get(image_url, stream=True)
    # Open a local file with wb ( write binary ) permission.
    local_file = open(r'C:\Users\brass\Desktop\Insta/Image/' + tag + str(n) + '.jpg', 'wb')
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True
    # Copy the response stream raw data to local image file.
    shutil.copyfileobj(resp.raw, local_file)
    # Remove the image url response object.
    n +=1
    del resp

driver.close()
