import requests
import BeautifulSoup
import re

"""
目标：
理解：
    搜索接口
    翻页    
"""

url = 'https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85'
login_url = 'https://login.taobao.com/member/login.jhtml'


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(type(r.text))
        return r.text[:1000]
    except:
        return "产生异常"


print(getHTMLText(url))
