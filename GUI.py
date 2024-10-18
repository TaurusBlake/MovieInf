import tkinter as tk
from tkinter import ttk
import MySQLdb
from PIL import Image, ImageTk
import requests
from io import BytesIO
import webbrowser
import link_mysql,more_page
import threading
import time

# 更新文字方塊的內容
def update_status(message):
    status_label.config(text=message)  
    
#清除資料庫舊資料，抓取新資料
def remove():
    def task():
        update_status("讀取中...")  # 顯示初始訊息

        # 模擬讀取過程，更新讀取狀態
        for i in range(1, 4):
            update_status(f"清除舊資料中...步驟 {i}/3")
            time.sleep(0.5)  # 模擬清除過程
        link_mysql.truncateData()  # 清除資料

        for i in range(1, 4):
            update_status(f"抓取新資料中...步驟 {i}/3")
            time.sleep(0.5)  # 模擬抓取過程
        more_page.catch()  # 抓取新資料

        update_status("資料更新完畢！請選擇影片。")  # 最後顯示更新完畢的訊息

        # 資料更新完畢後，重新載入 Combobox 內容
        all_combobox()
    
    # 創建新執行緒來執行 task 函數
    thread = threading.Thread(target=task)
    thread.start()
    
#顯示所有電影
def all_combobox():
    try:
        conn = MySQLdb.connect(host = "127.0.0.1",
                               user = "Taurus",
                               password = "12345678",
                               database = "movie_info",
                               port = 3306)
            
        cursor = conn.cursor()
        # 重新查詢資料庫獲取更新後的電影名稱
        sql = """SELECT title_chi FROM myvieshow WHERE show_date ORDER BY show_date"""
        cursor.execute(sql)
        results = cursor.fetchall()
        movie_titles = [row[0] for row in results]

        # 更新 Combobox 的值
        movie_combobox["values"] = movie_titles
        
        # 顯示查詢結果的總數
        total_count_label.config(text=f"電影總數: {len(movie_titles)}部")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print("資料庫連接失敗", e)
        
#顯示現正熱映
def hot_combobox():
    try:
        conn = MySQLdb.connect(host = "127.0.0.1",
                               user = "Taurus",
                               password = "12345678",
                               database = "movie_info",
                               port = 3306)
            
        cursor = conn.cursor()
        # 重新查詢資料庫獲取更新後的電影名稱
        sql = """SELECT title_chi FROM myvieshow WHERE show_date <= CURDATE() ORDER BY show_date"""
        cursor.execute(sql)
        results = cursor.fetchall()
        movie_titles = [row[0] for row in results]

        # 更新 Combobox 的值
        movie_combobox["values"] = movie_titles
        
        # 顯示查詢結果的總數
        total_count_label.config(text=f"現正熱映: {len(movie_titles)}部")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print("資料庫連接失敗", e)
        
#顯示即將上映
def pre_combobox():
    try:
        conn = MySQLdb.connect(host = "127.0.0.1",
                               user = "Taurus",
                               password = "12345678",
                               database = "movie_info",
                               port = 3306)
            
        cursor = conn.cursor()
        # 重新查詢資料庫獲取更新後的電影名稱
        sql = """SELECT title_chi FROM myvieshow WHERE show_date > CURDATE() ORDER BY show_date"""
        cursor.execute(sql)
        results = cursor.fetchall()
        movie_titles = [row[0] for row in results]

        # 更新 Combobox 的值
        movie_combobox["values"] = movie_titles
        
        # 顯示查詢結果的總數
        total_count_label.config(text=f"即將上映: {len(movie_titles)}部")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print("資料庫連接失敗", e)

#combobox選擇電影後
def search_movie():
    selected_movie = item_var.get()  # 抓combobox中選取的電影名稱
    try:
        conn = MySQLdb.connect(host = "127.0.0.1",
                                user = "Taurus",
                                password = "12345678",
                                database = "movie_info",
                                port = 3306)
        
        cursor = conn.cursor()
        sql_list = "SELECT * FROM myvieshow WHERE title_chi = %s "
        cursor.execute(sql_list, (selected_movie,))
        results1 = cursor.fetchall()
        
        if results1:
            movie_info_list = []
            for row in results1:
                # row 的資料依次為: 中文名稱, 英文名稱, 上映日期, 導演, 類型等
                movie_info_list = {
                    '中文名稱': row[1],
                    '英文名稱': row[2],
                    '上映日期': row[4],
                    '分級': row[3],
                    '類型': row[7],
                    '片長': row[8],
                    '導演': row[5],
                    '演員': row[6],
                    '劇情簡介': row[9],
                    # 可以添加更多欄位
                }
                
                image_url = row[11]
                video_url = row[12]
                
                # 顯示圖片
                display_image(image_url)
                
                # 當查詢到影片 URL 時，啟用顯示預告片按鈕
                trailer_btn.config(state=tk.NORMAL)  # 啟用按鈕
                trailer_btn.config(command=lambda: play_video(video_url)) 
            
            # 更新 Label 顯示資料
            chi_info.config(text=movie_info_list['中文名稱'])
            eng_info.config(text=movie_info_list['英文名稱'])
            date_info.config(text=movie_info_list['上映日期'])
            rating_info.config(text=movie_info_list['分級'])
            typ_info.config(text=movie_info_list['類型'])
            leng_info.config(text=movie_info_list['片長'])
            director_info.config(text=movie_info_list['導演'])
            actor_info.config(text=movie_info_list['演員'])
            story_info.config(text=movie_info_list['劇情簡介'])
    except Exception as e:
        print("資料庫連接失敗", e)
    finally:
        cursor.close()
        conn.close()

# 顯示圖片函式
def display_image(image_url):
    # 取得圖片
    response = requests.get(image_url)
    img_data = response.content

    # 使用Pillow將圖片轉換為Tkinter可顯示格式
    img = Image.open(BytesIO(img_data))
    img = img.resize((400, 550))  # 調整圖片大小
    tk_img = ImageTk.PhotoImage(img)

    # 創建Label並將圖片顯示在右上角
    img_label = tk.Label(win, image=tk_img)
    img_label.image = tk_img  # 防止圖片被回收
    img_label.place(x=800, y=100)  # 設置位置在右上角
    
# 在默認瀏覽器中打開 YouTube 影片
def play_video(video_url):
    webbrowser.open(video_url)

#建立tkinter視窗與標題
win = tk.Tk()
win.geometry('1280x800')
win.title("電影資訊查詢")

# 創建 Combobox
item_var = tk.StringVar()
movie_combobox = ttk.Combobox(win, width=50, textvariable=item_var)
movie_combobox.place(x=350, y=0)

# 初始刷新 Combobox 內容
all_combobox()


# 顯示查詢結果總數的 Label
total_count_label = tk.Label(win, text="電影數:", font=("Arial", 12))
total_count_label.place(x=220, y=0)

# 創建狀態顯示的文字方塊
status_label = tk.Label(win, text="請選擇影片...", font=("Arial", 12), fg="blue")
status_label.place(x=350, y=30)
    
# 創建更新資料按鈕
trailer_btn = tk.Button(win, text="更新資料庫",command=remove)
trailer_btn.place(x=1150, y=0)

# 創建所有電影按鈕
trailer_btn = tk.Button(win, text="所有電影",command=all_combobox)
trailer_btn.place(x=950, y=50)

# 創建現正熱映按鈕
trailer_btn = tk.Button(win, text="現正熱映",command=hot_combobox)
trailer_btn.place(x=1050, y=50)

# 創建即將上映按鈕
trailer_btn = tk.Button(win, text="即將上映",command=pre_combobox)
trailer_btn.place(x=1150, y=50)
   
# 創建查詢按鈕
search_btn = tk.Button(win, text="查詢", command=search_movie)
search_btn.place(x=850, y=0)
 
# 創建顯示預告片按鈕（預設為禁用狀態）
trailer_btn = tk.Button(win, text="顯示預告片", state=tk.DISABLED)
trailer_btn.place(x=950, y=0)
       
# 顯示Label
chi = tk.Label(win, text="電影名稱(中):")
chi.place(x=80, y=50)
chi_info = tk.Label(win, text="")
chi_info.place(x=180, y=50)
    
eng = tk.Label(win, text="電影名稱(英):")
eng.place(x=80, y=80)
eng_info = tk.Label(win, text="")
eng_info.place(x=180, y=80)
    
date = tk.Label(win, text="上  映  日  期:")
date.place(x=80, y=110)
date_info = tk.Label(win, text="")
date_info.place(x=180, y=110)
    
rating = tk.Label(win, text="分             級:")
rating.place(x=80, y=140)
rating_info = tk.Label(win, text="")
rating_info.place(x=180, y=140)
   
typ = tk.Label(win, text="類             型:")
typ.place(x=80, y=170)
typ_info = tk.Label(win, text="")
typ_info.place(x=180, y=170)
    
leng = tk.Label(win, text="片             長:")
leng.place(x=80, y=200)
leng_info = tk.Label(win, text="")
leng_info.place(x=180, y=200)
    
director = tk.Label(win, text="導             演:")
director.place(x=80, y=230)
director_info = tk.Label(win, text="")
director_info.place(x=180, y=230)
    
actor = tk.Label(win, text="演             員:")
actor.place(x=80, y=260)
actor_info = tk.Label(win, text="",wraplength=600,justify=tk.LEFT)
actor_info.place(x=80, y=285)
    
story = tk.Label(win, text="劇  情  簡  介:")
story.place(x=80, y=370)
story_info = tk.Label(win, text="",wraplength=600,justify=tk.LEFT)
story_info.place(x=80, y=395)
#建立循環等待使用者執行功能
win.mainloop()