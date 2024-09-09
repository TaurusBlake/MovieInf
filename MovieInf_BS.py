from bs4 import BeautifulSoup
import requests

def movie_list():
    url = "https://www.vscinemas.com.tw/vsweb/film/"
    web = requests.get(url+"index.aspx")
    soup = BeautifulSoup(web.text,"lxml")
    try:
        print("熱售中讀取成功")
        # 抓取頁數，找到pagebar中的所有li
        page = soup.find("section",class_="pagebar")
        page_amount = page.find_all("li")
        #印出按鈕數量確認
        # print(len(page_amount))
        try:
            links = []
            # 利用迴圈抓取連結，並丟入links空陣列
            for pages in range(len(page_amount)-2):
                # 使用 find_all 定位 到 class infoArea 標籤
                # 先抓取確定不會超過數量的位置，以便確認電影總數
                movie_amount = soup.find_all("section", class_="infoArea")
                # print(len(movie_amount))
                #利用迴圈抓取每部電影詳細介紹的連結，連結存於a的href中
                for movies in movie_amount:
                    link = movies.find("a")["href"]
                    links.append("https://www.vscinemas.com.tw/vsweb/film/"+link)
                #因為目前只有3頁，只需切換2次(目前此頁有5個按鈕，代表只有3頁，每次切換從第2頁開始)
                if pages+2 < len(page_amount)-1:
                    #它切按鈕會出錯因為網址會改變，改為使用網址的規律來切換頁面
                    web=requests.get(url+"index.aspx?p=%d" %(pages+2))
                    soup = BeautifulSoup(web.text,"lxml")
        
            try:
                web=requests.get(url+"coming.aspx")
                soup = BeautifulSoup(web.text,"lxml")
                print("即將上映讀取成功")
                # 利用迴圈抓取連結，並丟入links空陣列
                for pages in range(len(page_amount)-2):
                    # 使用 find_all 定位 到 class infoArea 標籤
                    # 先抓取確定不會超過數量的位置，以便確認電影總數
                    movie_amount = soup.find_all("section", class_="infoArea")
                    # print(len(movie_amount))
                    #利用迴圈抓取每部電影詳細介紹的連結，連結存於a的href中
                    for movies in movie_amount:
                        link = movies.find("a")["href"]
                        links.append("https://www.vscinemas.com.tw/vsweb/film/"+link)
                    #因為目前只有3頁，只需切換2次(目前此頁有5個按鈕，代表只有3頁，每次切換從第2頁開始)
                    if pages+2 < len(page_amount)-1:
                        #它切按鈕會出錯因為網址會改變，改為使用網址的規律來切換頁面
                        web=requests.get(url+"coming.aspx?p=%d" %(pages+2))
                        soup = BeautifulSoup(web.text,"lxml")
                        
            except Exception as e:
                print("威秀-即將上映連結抓取失敗", e)
        except Exception as e:
            print("威秀-熱售中連結抓取失敗", e)
    except Exception as e:
        print("網頁讀取失敗", e)
    
    return links