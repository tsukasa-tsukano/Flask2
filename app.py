from flask import Flask, render_template, session, request, redirect, url_for
import os

#インスタンスの作成
app = Flask(__name__)

#暗号鍵の作成
key = os.urandom(21)
app.secret_key = key

#idとパスワードの設定
id_pwd = {'tsukano':'D7Kd8Qr5'}

#メイン
#ログインセッションを持っていなければlogin,持っていればindexに飛ぶ
@app.route("/")
def index():
    if not session.get('login'):
        return redirect(url_for('login'))
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logincheck', methods=['POST'])
def logincheck():
    #login.htmlで入力されたデータを取り出す
    user_id = request.form['user_id']
    password = request.form['password']

#取得したユーザーIDとパスワードがid_pwdに含まれているか判定する
    if user_id in id_pwd:
        if password == id_pwd[user_id]:
            session['login'] = True
        else:
            session['login'] = False

    else:
        session['login'] = False
#redirect関数は引数に与えられたページへ転送する役割
    if session['login']:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('index'))

#アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)