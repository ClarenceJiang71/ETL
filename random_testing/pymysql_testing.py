import pymysql

conn = pymysql.connect(
    host='localhost', user='root', password='dbuserdbuser', 
    database='metadata', charset='utf8')

cursor = conn.cursor()
cursor.execute("show tables")
res =cursor.fetchall()
print(res)