from flask import Flask, render_template, request, redirect, session
from db import Database
import api

app = Flask(__name__)
dbo = Database()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get("users_name")
    email = request.form.get("users_email")
    password = request.form.get("users_password")

    response = dbo.insert(name, email, password)
    if response:
        return render_template('login.html', message="Registration Successful. Kindly login to proceed.")
    else:
        return render_template('register.html', message="Email already exists")


@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get("users_email")
    password = request.form.get("users_password")
    response = dbo.search(email, password)
    if response:
        return redirect('/profile')
    else:
        return render_template("login.html", message="Incorrect email/password")


@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/ner')
def ner():
    return render_template('ner.html')


@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text = request.form.get('ner_text')
    response = api.ner(text)
    print(response)
    return render_template('ner.html', response=response)


@app.route('/sentiment_analysis')
def sentiment_analysis():
    return render_template('sentiment_analysis.html')


@app.route('/perform_sentiment_analysis', methods=['post'])
def perform_sentiment_analysis():
    text = request.form.get('sentiment_analysis_text')
    response = api.sentiment_analysis(text)
    response = response['sentiment']
    response = max(response, key=lambda x: response[x])
    return render_template('sentiment_analysis.html', response=response)


# nd=d['sentiment']
# Key_max = max(nd, key = lambda x: nd[x])
# Key_max
app.run(debug=True)

# print(max(response['sentiment']))
