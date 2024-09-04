from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#使用selenium開啟chrome driver
driver = webdriver.Chrome()

url = "https://www.vscinemas.com.tw/vsweb/film/index.aspx"
# #等待3秒
# time.sleep(3)
# 隱式等待，等待指定的時間，然後再進行查詢，若指定時間找不到會拋出NoSuchElementException異常
driver.maximize_window()
driver.implicitly_wait(5)
# 取得指定網頁
driver.get(url)
# # page_source取得網頁原始碼
# print(driver.page_source)
try:
    print("網頁讀取成功")

    # 抓取頁數，找到pagebar中的所有li
    page = driver.find_element(By.CLASS_NAME, "pagebar")
    page_amount = page.find_elements(By.TAG_NAME, "li")
    
    links = []
    # 利用迴圈抓取連結，並丟入links空陣列
    for pages in range(len(page_amount)-2):
        print(pages)
        # 使用 XPath 定位 a 標籤並提取連結
        # 先抓取確定不會超過數量的位置，這裡選擇infArea，以便確認總數
        movie_amount = driver.find_elements(By.CLASS_NAME, "infoArea")  
        for movies in range(len(movie_amount)):
            element = driver.find_element(By.XPATH, "/html/body/article/ul/li[%d]/figure/a" %(movies+1))
            link = element.get_attribute("href")
            links.append(link)
        if pages+2 < len(page_amount)-1:
            driver.get(url+"?p=%d" %(pages+2))
        time.sleep(5)
    # print(len(links))


except Exception as e:
    print("連線失敗",e)
driver.quit()