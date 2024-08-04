import sqlite3 #Importar o pacote do banco de dados sqlite

con = sqlite3.connect('database.db') #Faz a conexão com o banco de dados

con.execute('CREATE TABLE users(email VARCHAR(255), password TEXT)') # CRIA A TABELA DE USUÁRIOS

con.close() # FECHA A CONEXÃO