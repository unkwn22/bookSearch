from flask import Flask, render_template, jsonify, request, session

app = Flask(__name__)

from pymongo import MongoClient

import bcrypt

client = MongoClient('localhost', 27017)
db = client.accountdata


# doc = {'id': 'lsjc12911', 'pass': 'lsjc12911'}
# db.users.insert_one(doc)

## HTML 화면 보여주기
@app.route('/')
def main_page():
    return render_template('login.html')

#함수
@app.route('/login', methods=['POST'])
def login():
    id_receive = request.form['id_give']
    pass_receive = request.form['pass_give']
    existing_user = user = db.users.find_one({'id': id_receive})

    if existing_user is not None:
        password = user['pass']
        if pass_receive == password:
            return jsonify({'check': 1})
        else:
            print("Invalid Password")
            return jsonify({'check': 3})
    else:
        print("Invalid Username")
        return jsonify({'check': 2})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
