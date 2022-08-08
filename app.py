
import pymysql

 
import pymysql 

conn = pymysql.connect(host='http://database-1.cceupqtdw2si.ap-northeast-2.rds.amazonaws.com', user='root', password='GOORM0808', db='goorm', charset='utf8') 
cursor = conn.cursor() 

sql = '''CREATE TABLE user ( 
id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
email varchar(255), 
department varchar(255) 
) 
''' 

cursor.execute(sql) 

conn.commit() 
conn.close() 
