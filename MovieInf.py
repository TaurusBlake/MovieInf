from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# import time

# # 創建 Chrome 瀏覽器選項，不開啟畫面執行爬蟲
# options = Options()
# options.add_argument("--headless")  # 設定為無頭模式
# options.add_argument("--disable-gpu")  # 禁用 GPU
# #使用selenium開啟chrome driver
# driver = webdriver.Chrome(options=options)

#使用selenium開啟chrome driver
driver = webdriver.Chrome()

url_hot = "https://www.vscinemas.com.tw/vsweb/film/index.aspx"

# 隱式等待，等待指定的時間，然後再進行查詢，若指定時間找不到會拋出NoSuchElementException異常
driver.maximize_window()
driver.implicitly_wait(5)
# 取得指定網頁
driver.get(url_hot)
# # page_source取得網頁原始碼
# print(driver.page_source)
try:
    print("熱售中讀取成功")

    # 抓取頁數，找到pagebar中的所有li
    page = driver.find_element(By.CLASS_NAME, "pagebar")
    page_amount = page.find_elements(By.TAG_NAME, "li")
    #印出按鈕數量確認
    # print(len(page_amount))
    
    links = []
    # 利用迴圈抓取連結，並丟入links空陣列
    for pages in range(len(page_amount)-2):
        # 使用 XPath 定位 a 標籤並提取連結
        # 先抓取確定不會超過數量的位置，這裡選擇infArea，以便確認電影總數
        movie_amount = driver.find_elements(By.CLASS_NAME, "infoArea")
        #利用迴圈抓取每部電影詳細介紹的連結
        for movies in range(len(movie_amount)):
            element = driver.find_element(By.XPATH, "/html/body/article/ul/li[%d]/figure/a" %(movies+1))
            link = element.get_attribute("href")
            links.append(link)
        #因為目前只有3頁，只需切換2次(目前此頁有5個按鈕，代表只有3頁，每次切換從第2頁開始)
        if pages+2 < len(page_amount)-1:
            #它切按鈕會出錯因為網址會改變，改為使用網址的規律來切換頁面
            driver.get(url_hot+"?p=%d" %(pages+2))
        driver.implicitly_wait(5)
        # time.sleep(5)
    #切換到即將上映   
    url_com = "https://www.vscinemas.com.tw/vsweb/film/coming.aspx"
    driver.get(url_com)
    try:
        print("即將上映讀取成功")
        #抓取頁數
        page = driver.find_element(By.CLASS_NAME, "pagebar")
        page_amount = page.find_elements(By.TAG_NAME, "li")
        #印出按鈕數量確認
        # print(len(page_amount))
        for pages in range(len(page_amount)-2):
            # 使用 XPath 定位 a 標籤並提取連結
            # 先抓取確定不會超過數量的位置，這裡選擇infArea，以便確認電影總數
            movie_amount = driver.find_elements(By.CLASS_NAME, "infoArea")
            #利用迴圈抓取每部電影詳細介紹的連結
            for movies in range(len(movie_amount)):
                element = driver.find_element(By.XPATH, "/html/body/article/ul/li[%d]/figure/a" %(movies+1))
                link = element.get_attribute("href")
                links.append(link)
            #因為目前只有3頁，只需切換2次(目前此頁有4個按鈕，代表只有2頁，每次切換從第2頁開始)
            if pages+2 < len(page_amount)-1:
                #它切按鈕會出錯因為網址會改變，改為使用網址的規律來切換頁面
                driver.get(url_com+"?p=%d" %(pages+2))
            driver.implicitly_wait(5)
        
        
        
    except Exception as e:
        print("即將上映頁面讀取失敗", e)
    


except Exception as e:
    print("連線失敗", e)
driver.quit()