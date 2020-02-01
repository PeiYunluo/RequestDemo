import requests

try:
    kv ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    kv2 ={'wd':'python'}
    r = requests.get('https://www.baidu.com/s',params=kv2,headers = kv)
    print(r.request.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:])
except:
    print('888888888888888888888888888888888888')
