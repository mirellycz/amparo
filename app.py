from flask import Flask, render_template, flash, redirect, request, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = "Karol1004"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form['email']
    senha = request.form['senha']
    if email == 'karol' and senha == 'senha123':
        flash('Login feito com sucesso, você está logado','sucess')
        return render_template('/index.html')
    else:
        flash('Dados incorretos. Email ou senha inválidos', 'danger')
        return redirect(url_for('login'))
    


@app.route('/doacoes')
def doacoes():
     return render_template('doacoes.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')










