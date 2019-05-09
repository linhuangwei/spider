import requests
import re

basic_url = 'https://detail.tmall.com/item.htm?spm=a1z10.1-b-s.w4006-14989492066.43.4fbc2435tZQEkO&id=564430245247&rn=69a35ef3de5a285850a7578a2fb2a0cd&abbucket=4&skuId=3566849937526&scene=taobao_shop'

headers = {
    "cookie": "cna=k7kBE8cvMk8CAa8raL7Vchh/; lid=%E5%BF%83%E8%8B%A5%E5%90%91%E9%98%B3%E4%BD%95%E6%83%A7%E9%A3%8E%E6%B5%AAhw; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; hng=CN%7Czh-CN%7CCNY%7C156; t=ca885a784324b0522b7037062004662c; tracknick=%5Cu5FC3%5Cu82E5%5Cu5411%5Cu9633%5Cu4F55%5Cu60E7%5Cu98CE%5Cu6D6Ahw; _tb_token_=e3696d4e9a3b3; cookie2=1771d23691daec86f735a61f66cb1b60; _m_h5_tk=09b84feea10e07fc691f984c31aaabf5_1557405727920; _m_h5_tk_enc=6b5e07d255d966c1f58f4153c51e096a; dnk=%5Cu5FC3%5Cu82E5%5Cu5411%5Cu9633%5Cu4F55%5Cu60E7%5Cu98CE%5Cu6D6Ahw; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ48ZnaTNslA%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEa%2BocMaxvuWc8E%3D&id2=UUGjMBCrsCM6hA%3D%3D&nk2=s0yiXhy4Sd0A9AghLwLSCYho&lg2=V32FPkk%2Fw0dUvg%3D%3D; _l_g_=Ug%3D%3D; unb=2912950709; lgc=%5Cu5FC3%5Cu82E5%5Cu5411%5Cu9633%5Cu4F55%5Cu60E7%5Cu98CE%5Cu6D6Ahw; cookie1=BxUEcQt0GYkbmI7d4rf9YAddsWUgTNPBiO4tnaPRi84%3D; login=true; cookie17=UUGjMBCrsCM6hA%3D%3D; _nk_=%5Cu5FC3%5Cu82E5%5Cu5411%5Cu9633%5Cu4F55%5Cu60E7%5Cu98CE%5Cu6D6Ahw; sg=w93; csg=19c83e37; x=__ll%3D-1%26_ato%3D0; x5sec=7b22726174656d616e616765723b32223a226131656230663730393165366437393062623030346636613634653565366261434c714c304f5946454f53416c4e6e4569744b4f5a426f4d4d6a6b784d6a6b314d4463774f547378227d; whl=-1%260%260%260; l=bBI4VGDcvaR0HUeaBOfZ5uI8Up_9ZIRbzsPzw49g3ICPOXfX-ubAWZ9JLDLWC3GVa6L6R3RYGVWzBAYTJyUBl; isg=BNXVELS8JcDJlwelB7JtSb3E5NFPeot17gd0vVd6UMyBrvegHyB9tHkoePK9rqGc",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def get_page(url):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print(e)


def get_info(page):
    try:
        items = re.findall(r'"rateContent":"(.*?)"', page, re.S)
        for item in items:
            yield item
    except Exception as e:
        print(e)


def save_data(datas):
    with open("E:\\淘宝评论.txt", "a", encoding="utf-8") as f:
        for data in datas:
            f.write(data)
            f.write('\n')
        f.close()


urls = [
    'https://rate.tmall.com/list_detail_rate.htm?itemId=564430245247&spuId=925720635&sellerId=420722466&order=3&currentPage={}&append=0&content=1'.format(i) for i in range(1, 31)]

for url in urls:
    page = get_page(url)
    print(url)
    datas = get_info(page)
    save_data(datas)
