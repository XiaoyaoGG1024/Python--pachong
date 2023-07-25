from lxml import etree
import requests
import re
import pymysql
url='https://movie.douban.com/top250'
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
response=requests.get(url,headers=header)
h=response.text
html=etree.HTML(h)
tiitle=html.xpath("//div[@class]/a/span[@class][1.csv]/text()")
year=re.findall(r'.*(\d{4})&nbsp;/&nbsp;.*',h)
pingfen=html.xpath("//div[@class]/span[@class='rating_num']/text()")
conn=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password='123456',
    db='douban')
cursor=conn.cursor()
sql_createtable=" create table mv(title varchar(200),year varchar(10),pingfen varchar(10));"
cursor.execute(sql_createtable)
for i in range(len(year)):
    sql_insert="insert mv(title,year,pingfen)value(%s,%s,%s);"
    cursor.execute(sql_insert,(tiitle[i],year[i],pingfen[i]))
sql_select="select pingfen from mv order by  pingfen desc  limit 5;"
cursor.execute(sql_select)
s1=cursor.fetchall()
print(s1)
conn.commit()
cursor.close()
conn.close()
