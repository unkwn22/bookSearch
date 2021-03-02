from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "hello"

from pymongo import MongoClient

import bcrypt

client = MongoClient('localhost', 27017)
db = client.accountdata


# HTML 화면 보여주기
@app.route('/login')
def ren_main():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    id_receive = request.form['id_give']
    pass_receive = request.form['pass_give'].encode('utf-8')
    existing_user = db.users.find_one({'id': id_receive})

    if existing_user is not None:
        # password = existing_user['pass']
        if pass_receive == existing_user['pass']:
            session["user"] = id_receive
            # return jsonify({'check': 1})
            return redirect(url_for("user"))
        else:
            return jsonify({'check': 3})
    else:
        return jsonify({'check': 2})


@app.route('/signup')
def ren_Signup():
    return render_template('signup.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        name_receive = request.form['name_give']
        id_receive = request.form['id_give']
        pass_receive = request.form['pass_give'].encode('utf-8')
        existing_user = db.users.find_one({'id': id_receive})

        if existing_user is not None:
            return jsonify({'check': 1})
        else:
            doc = {'name': name_receive, 'id': id_receive, 'pass': pass_receive}
            db.users.insert_one(doc)
            return jsonify({'check': 2})


# @app.route('/example')
# def ren_ex():
#     return render_template('example.html')


@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        print("session name"+user)
        



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
