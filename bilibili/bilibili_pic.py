
import requests
import re

"""
    date:2022-01-27
    author:逍遥哥哥每天都要努力啊（csdn）
"""

# https://www.bilibili.com/v/dance/otaku/?spm_id_from=333.5.b_64616e63655f6f74616b75.3#/2423/default/0/1/
# https://www.bilibili.com/v/dance/otaku/?spm_id_from=333.5.b_64616e63655f6f74616b75.3#/2423/default/0/2/
#https://www.bilibili.com/v/dance/otaku/?spm_id_from=333.5.b_64616e63655f6f74616b75.3#/2423/click/0/400/2022-01-20,2022-01-27
#https://www.bilibili.com/v/dance/otaku/?spm_id_from=333.5.b_64616e63655f6f74616b75.3#/2423/click/0/{page}/2022-01-20,2022-01-27
#https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&order=click&copy_right=-1&cate_id=20&page=2&pagesize=20&jsonp=jsonp&time_from=20220121&time_to=20220128&keyword=可爱&callback=jsonCallback_bili_69676205122123624


def lxml(page):
    url = f'https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&order=click&copy_right=-1&cate_id=20&page={page}&pagesize=20&jsonp=jsonp&time_from=20230101&time_to=20230117&keyword=可爱&callback=jsonCallback_bili_69676205122123624'
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
    response = requests.get(url, headers=headers)
    # print(response.encoding) utf-8
    #'unicode_escape'
    h = response.content.decode('unicode_escape')
    print(f"正在获取第{page}页")
    return   h

def dow(html):
    pic_tmp = re.findall(r'"pic":"(.*?)"', html)
    author=re.findall(r'"author":"(.*?)"', html)
    for i in range(len(pic_tmp)):
        pic=str(pic_tmp[i]).replace("\\","")
        # file_name=pic.replace("/","").replace(".jpg","")
        with open('./pic/'+author[i]+'.jpg', 'wb') as file:
            file.write(requests.get('http:'+pic).content)

if __name__ == '__main__':
    start_page = int(input("请输入开始页面:"))
    end_page = int(input("请输入结束页面:"))
    for page in range(start_page, end_page + 1):
        dow(lxml(page))

