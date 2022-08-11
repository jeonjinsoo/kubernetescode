import pymysql 

conn = pymysql.connect(host='database-1.cceupqtdw2si.ap-northeast-2.rds.amazonaws.com', user='admin', password='goorm0808'=, charset='utf8', port=3306) 


cursor = conn.cursor() 

sql = "CREATE DATABASE exercise"


cursor.execute(sql)

conn.commit() 
conn.close()
