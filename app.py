from flask import Flask, render_template, flash, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/doacoes')
def doacoes():
    return render_template('doacoes.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')




