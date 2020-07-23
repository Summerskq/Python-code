import pymysql
conn = pymysql.connect(host='localhost',user='root',passwd="123",db='linux')
cur = conn.cursor()
select_sql = "select * from skq"
cur.execute(select_sql)
print(cur.fetchall())
