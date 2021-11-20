from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import time
import csv
import pandas as pd

def tag_searching(word):
    url = "https://www.best-hashtags.com/hashtag/" + str(word)
    return url

driver = webdriver.Chrome(r'C:\Users\brass\PycharmProjects\newGoogle\chromedriver') #경로변경할것
driver.get('https://www.best-hashtags.com')
time.sleep(2)

word = input("검색어를 입력하세요 : ")
word = str(word)
url = tag_searching(word)

driver.get(url)
time.sleep(1)

results = []

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

content1 = soup.select('p1')[0].text
content2 = soup.select('p2')[0].text

    #해시태그
tag1 = re.findall(r'#[^\s#,\\]+', content1)
tag2 = re.findall(r'#[^\s#,\\]+', content2)

data = [content1, content2, tag1, tag2]

results.append(data)

print(results)

results_df = pd.DataFrame(results)
results_df.columns = ['content1', 'content2', 'tag1', 'tag2']
results_df.to_csv(r'C:\Users\brass\PycharmProjects\newGoogle\result.csv',index=False, encoding="utf-8-sig") #경로 바꾸세요
