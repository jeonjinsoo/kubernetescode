import pymysql 

conn = pymysql.connect(host='database-1.cceupqtdw2si.ap-northeast-2.rds.amazonaws.com', user='admin', password='GOORM0808', db='goorm', charset='utf8', port=3306) 

''' 
cursor = db.cursor() 

sql = """
    INSERT INTO user VALUES('aa','aa');
"""

cursor.execute(sql)

db.commit()

db.close()



