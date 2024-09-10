from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import pandas as pd



# 創建 Chrome 瀏覽器選項，不開啟畫面執行爬蟲
options = Options()
options.add_argument("--headless")  # 設定為無頭模式
options.add_argument("--disable-gpu")  # 禁用 GPU
#使用selenium開啟chrome driver
driver = webdriver.Chrome(options=options)

url = "https://www.vscinemas.com.tw/vsweb/film/detail.aspx?id=7457"
web = requests.get(url)
soup = BeautifulSoup(web.text, "lxml")
page = soup.find("div",class_="movieMain")
# 建構空list暫存內容
total_inf=[]
movieInf_list = []
# 爬取圖片
img_link = page.find("img")["src"]
img = img_link.replace("..","https://www.vscinemas.com.tw/vsweb")
web_img = requests.get(img)
img1 = web_img.content
with open("0.jpg","wb") as file:
    file.write(img1)

# # 爬取標題
# title_chi = page.find("h1").text
# title_eng = page.find("h2").text
# #上映日(冒號是全形)
# whole_date = page.find("time").text.split("：")
# date_time = pd.to_datetime(whole_date[1])#將字串轉為日期格式
# date = date_time.date() #提取日期
# # 導演、演員、類型、片長
# movie_info = page.find_all("td")
# for item in movie_info:
#     movieInf_list.append(item.text)
# movie_time = " ".join(movieInf_list[7]).replace(" ", "")

# # date = page[3].split("：") #將上映日切開，只取得日期
# # long = " ".join(page[13:17]).replace(" ", "")#將片長合併，並去掉空白

# # 打开目标页面，抓取分級(藏在CSS中，使用selenium)
# driver.get(url)
# # 找到目标元素
# rating_url = driver.find_element(By.XPATH, "/html/body/article/section/div[2]/section/div[1]/span[1]")
# # 使用 JavaScript 获取伪元素的内容(影片分級)
# rating_text = driver.execute_script(
#     "return window.getComputedStyle(arguments[0], '::before').getPropertyValue('content');",
#     rating_url)
# # print(rating_text)

# # 抓取劇情簡介
# check_story = soup.find("div",class_="bbsArticle").text.strip().split("－全台預售情報 ")
# movieInf_list.append(check_story)
# story = movieInf_list[8][0]


# # 建構有表頭的dataframe，存放資訊
# info = {"電影名(中)":[title_chi],"電影名(英)":[title_eng],"分級":[rating_text],"上映日":[date],
#         "導演":[movieInf_list[1]],"演員":[movieInf_list[3]],"類型":[movieInf_list[5]],
#         "片長":[movieInf_list[7]],"劇情介紹":[story]}
# movie = pd.DataFrame(info)

# 抓取預告片連結


# movie.loc[0]=inf
# movie.to_csv("movie.csv", index=False)




# 关闭浏览器
# driver.quit()