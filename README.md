># 前言
>>這是一個利用網路爬蟲，爬取威秀網站資訊的程式，    
>>未來可能會再添加其他影城的資訊，  
>>觀迎大家來跟我交流，並給予我指教。  
>>我所有的程式碼與物件都僅作為學習使用，請不要用於營利。  
>>如果有侵犯到版權，請隨時通知我移除。  
>>謝謝你們 ^__^    
>>This is a program that uses a web crawler to crawl information from the Village Roadshow website.
>>In the future, information about other movie theaters may be added.
>>Everyone is welcome to communicate with me and give me advice.
>>All my codes and objects are only used for learning, please do not use them for profit.
>>If there is any copyright infringement, please notify me at any time to remove it.
>>Thank you ^__^
># 遊戲畫面
>><img src="https://github.com/TaurusBlake/MovieInf/blob/main/View/mov0.png" alt="Editor" width="300">
>><img src="https://github.com/TaurusBlake/MovieInf/blob/main/View/mov1.png" alt="Editor" width="300">
>><img src="https://github.com/TaurusBlake/MovieInf/blob/main/View/mov2.png" alt="Editor" width="300">  
>><img src="https://github.com/TaurusBlake/MovieInf/blob/main/View/mov3.png" alt="Editor" width="300">  
># 安裝
>>打包下載  
>>需要建立資料庫，本版使用MariaDB存取資料  
>>程式碼中連接資料庫部分須改為本地端使用者的資料庫  
>>Table格式如下，可直接複製使用  
>>CREATE TABLE IF NOT EXISTS myvieshow  
>>(	ID INT,  
>>	title_chi VARCHAR(200),  
>>	title_eng VARCHAR(200),   
>>	rating VARCHAR(5),  
>>  show_date date,   
>>	director VARCHAR(50),   
>>	actor VARCHAR(20050),  
>>	movie_type VARCHAR(25),  
>>	movie_length VARCHAR(10),  
>>  story VARCHAR(2000),  
>>	movie_url VARCHAR(100),  
>>	img_url VARCHAR(100),  
>>	trailer_url VARCHAR(100))  
># 文件說明
>>├──View(簡介圖像)  
>>├──MovieInf_BS.py(抓取所有電影連結)  
>>├──more_page.py(透過連結抓取每頁資料)  
>>├──link_mysql.py(連接資料庫的自訂函式)  
>>├──GUI.py(顯示面板)  
>>└──movies.csv(抓取的資料會同時輸出成csv檔)  
>>  
># 作者
>>**TaurusBlake**  
>>**email**:shamgarxie@gmail.com
