from selenium import webdriver
from bs4 import BeautifulSoup as soups

def search_selenium(search_name, search_path, search_limit) :
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    
    browser = webdriver.Chrome(r"C:\Users\brass\PycharmProjects\newGoogle\chromedriver")
    browser.get(search_url)
    
    image_count = len(browser.find_elements_by_tag_name("img"))
    
    print("로드된 이미지 개수 : ", image_count)

    browser.implicitly_wait(2)

    if search_limit <= 450:
        for i in range( search_limit ) :
            image = browser.find_elements_by_tag_name("img")[i]
            image.screenshot(search_name + str(i) + ".png")
    else:
        for i in range( 450 ) :
            image = browser.find_elements_by_tag_name("img")[i]
            image.screenshot(search_name + str(i) + ".png")
        browser.find_element_by_xpath('//input[@type="button"]').click()
        for i in range( search_limit - 450 ) :
            image = browser.find_elements_by_tag_name("img")[i]
            image.screenshot(search_name + str(i) + ".png")


    browser.close()

if __name__ == "__main__" :

    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    search_path = r"C:\Users\sam56\Desktop\구글크롤러\img"
    # search_maybe(search_name, search_limit, search_path)
    search_selenium(search_name, search_path, search_limit)
