import pymysql 
conn=pymysql.connect(host='localhost',user='root',password='',db='mini_pro')
a=conn.cursor()
sql= "select path from files where id=1"
a.execute(sql)
data=a.fetchone()
value=data[0]
print(value)