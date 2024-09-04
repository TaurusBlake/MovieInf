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
    # tag = driver.find_element(By.CLASS_NAME,"indexNews")
    # tags = tag.find_elements(By.TAG_NAME,"li")
    # for inf in tags:
    #     print(inf.text)
    # 使用 XPath 定位 a 標籤並提取連結
    amount = driver.find_elements(By.CLASS_NAME, "infoArea")
    links = []
    for i in range(len(amount)):
        element = driver.find_element(By.XPATH, "/html/body/article/ul/li[%i]/figure/a" %(i+1))
        link = element.get_attribute("href")
        links.append(link)
    print(len(links))  # 印出提取到的連結


except Exception as e:
    print("連線失敗",e)
time.sleep(5)
driver.quit()