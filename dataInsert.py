import json
from collections import OrderedDict

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


# books_data = OrderedDict()
#
# book = []
#
# for tr in trsAni:
#     if tr is not None:
#         book_img = tr.select_one('dl > div > div > a > img')['src']
#         book_title = tr.select_one('dl > div > div > a > img')['alt']
#         book_url = tr.select_one('dl > div > div > a')['href']
#         print(book_img,book_title,book_url)
#         books_data.append({'book_img': book_img,
#                            'book_title': book_title,
#                            'book_url': book_url})
#
#         book = {'book' : books_data}
#
#
#
# print(json.dumps(book,ensure_ascii=False,indent='\t'))

def get_img():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://book.naver.com/bestsell/bestseller_list.nhn?type=image&cp=yes24&cate=001001022', headers=headers)
    dataAni = requests.get(
        'https://book.naver.com/bestsell/bestseller_list.nhn?cp=yes24&cate=001001008&bestWeek=2021-02-3&indexCount=25&type=image',
        headers=headers)
    dataIt = requests.get(
        'https://book.naver.com/bestsell/bestseller_list.nhn?cp=yes24&cate=001001003&bestWeek=2021-02-3&indexCount=18&type=image',
        headers=headers)
    dataFant = requests.get(
        'https://book.naver.com/bestsell/bestseller_list.nhn?cp=yes24&cate=001001044&bestWeek=2021-02-3&indexCount=2&type=image',
        headers=headers)
    dataChildren = requests.get(
        'https://book.naver.com/bestsell/bestseller_list.nhn?cp=yes24&cate=001001016&bestWeek=2021-02-3&indexCount=6&type=image',
        headers=headers)
    dataHistory = requests.get(
        'https://book.naver.com/bestsell/bestseller_list.nhn?cp=yes24&cate=001001010&bestWeek=2021-02-3&indexCount=9&type=image',
        headers=headers)
    soup = BeautifulSoup(dataHistory.text, 'html.parser')


    trs = soup.select('#section_bestseller > ol > li')

    for tr in trs:
        book_img = tr.select_one('dl > div > div > a > img')['src']
        book_title = tr.select_one('dl > div > div > a > img')['alt']
        book_url = tr.select_one('dl > div > div > a')['href']
        if book_img is not None:
            doc = {
                'img' : book_img,
                'title' : book_title,
                'url' : book_url,
                'category' : '역사와문학'
            }

            db.book.insert_one(doc)
            print('완료!',book_title)

get_img()





