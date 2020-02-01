import requests

url = 'https://www.nationalgeographic.com/content/dam/science/2020/01/22/shum-laka/01_shumlaka_excavation-of-a-double-burial-at-the-shum-laka-rock-shelter.adapt.1900.1.jpg'
path = "D:/picture.jpg"
try:
    r = requests.get(url)
    print(r.status_code)
    with open(path,'wb') as f:
        f.write(r.content)
        f.close()
except:
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaa')