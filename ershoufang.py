from lxml import etree
import requests
import re
url='https://cs.lianjia.com/ershoufang/'
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
response=requests.get(url,headers=header)
h=response.text
html=etree.HTML(h)
title=html.xpath("//div[@class]/ul[@class]/li[@class]/div[@class]/div[@class='title']/a/text()")
price=html.xpath("//div[@class='totalPrice totalPrice2']/span/text()")
address=html.xpath("//div[@class]/ul[@class]/li[@class]/div[@class='info clear']//div[@class='positionInfo']/a[2]/text()")
for i in range(len(title)):
    print(str(title[i]).replace(" ",',')+'\t'+price[i]+'\t'+address[i])