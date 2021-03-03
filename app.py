import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
import pandas as pd
import json
from collections import OrderedDict

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

books = list(db.book.find({},{'_id' : False}))
my_list = []
for book in books:
    b_category = book['category']
    if b_category not in my_list:
        my_list.append(b_category)

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html', books=books, my_list=my_list)

# book의 정보들을 뿌려주는 API
@app.route('/api/books', methods=['GET'])
def show_books():
    books_data = list(db.book.find({}, {'_id':False}))
    return jsonify({'books_data': books_data})


# 검색하기(POST) API
@app.route('/api/search_book', methods=['POST'])
def search_book():
    bookCategory_receive = request.form['bookCategory']
    searchValue_receive = request.form['searchValue']

    category = my_list[int(bookCategory_receive) - 1]
    print(category)

    df = pd.DataFrame(list(db.book.find({'category':category},{'_id':False})))
    img_list = []
    title_list = []
    url_list = []
    collect_book = OrderedDict()

    img_list = df[df['title'].str.contains(searchValue_receive)]['img']
    title_list = df[df['title'].str.contains(searchValue_receive)]['title']
    url_list = df[df['title'].str.contains(searchValue_receive)]['url']

    # collect_book = OrderedDict()
    # c_book = []
    # for flag in b_list:  # 0- len(df)까지
    #     if flag:
    #         for i in range(0,len(df)):
    #             collect_book.append({ 'img' : df['img'][i],
    #                               'title' : df['title'][i],
    #                               'url' : df['url'][i]})
    #
    collect_book = {
                    'img_list' : img_list,
                    'title_list' : title_list,
                    'url_list' : url_list
                    }
    # print(collect_book['img_list'][1])
    # print(df['title'])

    # db.orders.insert_one(doc)
    return jsonify({'msg': ' 저장 '})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)



