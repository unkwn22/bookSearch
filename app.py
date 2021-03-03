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


# 검색하기(POST)-카테고리가 있을 때 API
@app.route('/api/search_book/category', methods=['POST'])
def search_book_with_category():
    bookCategory_receive = request.form['bookCategory']
    searchValue_receive = request.form['searchValue']

    category = my_list[int(bookCategory_receive) - 1]
    print(category)

    book_data = list(db.book.find({'category': category}, {'_id': False}))
    print(book_data)


    return jsonify({'msg': ' 저장 ','book_data':book_data,'searchValue_receive':searchValue_receive})


# 검색하기(POST)-카테고리가 없을 때 API
@app.route('/api/search_book', methods=['POST'])
def search_book():
    searchValue_receive = request.form['searchValue']

    book_data = list(db.book.find({}, {'_id': False}))
    print(book_data)


    return jsonify({'msg': ' 저장 ','book_data':book_data,'searchValue_receive':searchValue_receive})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)



