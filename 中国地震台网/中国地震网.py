import re
import requests
import json
with open('data/中国地质网.csv', 'a+', encoding='gb18030') as file :
    file.writelines('震级M,发震时刻(UTC+8),纬度(°),经度(°),深度(KM),参考位置\n')
for i in range(1, 506) :
    print("正在爬取第"+str(i)+"页数据")
    url = f'http://www.ceic.ac.cn/ajax/search?page={i}&&start=2010-01-01&&end=2022-5-01' \
          '&&jingdu1=&&jingdu2=&&weidu1=&&weidu2=&&height1=&&height2=&&zhenji1=&&zhenji2=&&' \
          'callback=jQuery18008396570517882946_1640587328683&_=1640587342462'
    hearders = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                               " AppleWebKit/537.36 (KHTML, like Gecko)"
                               " Chrome/93.0.4577.82 Safari/537.36" }
    response = requests.get(url, headers=hearders)
    #将后面没用的字段删除
    h = response.text.replace('jQuery18008396570517882946_1640587328683(', '').replace(')', '')
    #加载为字典类型
    html = json.loads(h)
    #因为我们保存的是字典类型所以要进行强转str
    zhnegjiM = re.findall(r" 'M': '(.*?)',", str(html))
    shijian = re.findall(r"'O_TIME': '(.*?)',", str(html))
    weidu = re.findall(r"'EPI_LAT': '(.*?)',", str(html))
    jingdu = re.findall(r"'EPI_LON': '(.*?)',", str(html))
    shengdu = re.findall(r"'EPI_DEPTH': (.*?),", str(html))
    cankaoweizhi = re.findall(r"'LOCATION_C': '(.*?)',", str(html))
    with open('data/中国地质网.csv', 'a', encoding='gb18030') as file :
        for i in range(len(zhnegjiM)) :
            file.writelines(zhnegjiM[i] + ',' + shijian[i] + ',' + weidu[i] + ',' + jingdu[i] +','+shengdu[i]+ ',' + cankaoweizhi[i] + '\n')
