import MySQLdb


def mysql(ID,title_chi,title_eng,rating_text,show_date,direct,actor,
          movie_type, movie_length,story,link):
    try:
        conn = MySQLdb.connect(host = "127.0.0.1",
                               user = "root",
                               password = "0912249031",
                               database = "movieinfo",
                               port = 3306)
        
        cursor = conn.cursor()
        
        #創建表格
        sql = """INSERT INTO vieshow (ID ,title_chi ,title_eng, rating,
                show_date, director, actor, movie_type, movie_length,
                story, link)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        var = (ID,title_chi,title_eng,rating_text,show_date,direct,actor,
               movie_type,movie_length,story,link)
                
        cursor.execute(sql,var)
        conn.commit()
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print("資料庫連接失敗",e)