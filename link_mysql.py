import MySQLdb

def truncateData():
    try:
        conn = MySQLdb.connect(host = "127.0.0.1",
                                user = "Taurus",
                                password = "12345678",
                                database = "movie_info",
                                port = 3306)
        cursor = conn.cursor()
        
        #匯入資料
        sql = """truncate TABLE myvieshow"""

        cursor.execute(sql)
        conn.commit()
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print("資料庫連接失敗",e)

#將資料寫入MySQL
def mysql(ID,title_chi,title_eng,rating_text,show_date,direct,actor,
          movie_type, movie_length,story,movie_url,img_url,trailer_url):
    try:
        conn = MySQLdb.connect(host = "127.0.0.1",
                               user = "Taurus",
                               password = "12345678",
                               database = "movie_info",
                               port = 3306)
        
        cursor = conn.cursor()
        
        #匯入資料
        sql = """INSERT INTO myvieshow (ID ,title_chi ,title_eng, rating,
                show_date, director, actor, movie_type, movie_length,
                story, movie_url,img_url,trailer_url)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        var = (ID,title_chi,title_eng,rating_text,show_date,direct,actor,
               movie_type,movie_length,story,movie_url,img_url,trailer_url)
                
        cursor.execute(sql,var)
        conn.commit()
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print("資料庫連接失敗",e)