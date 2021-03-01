from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.accountdata


# doc = {'id': 'lsjc12911', 'pass': 'lsjc12911'}
# db.users.insert_one(doc)

## HTML 화면 보여주기
@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['CHECK'])
def check_id():
    id_receive = request.form['id_give']
    pass_receive = request.form['pass_give']

    user = db.users.find_one({'id': id_receive})


    if user is not None:
        if pass_receive is not
    else:
        print("없는 아이디입니다")

    return jsonify({'msg': '하이!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
