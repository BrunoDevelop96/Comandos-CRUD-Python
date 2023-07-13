#---------Conexão com banco de dados mysql-------------
import mysql.connector

conexao = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='bruno1996',
    database ='bd_crud',
)
cursor = conexao.cursor() #conexão
#---------Conexão com banco de dados mysql-------------

#----------------CREATE-----------------
nome_produto = "coca-cola"
valor = 4

comando = f'INSERT INTO vendas(nome_produto, valor) VALUES ("{nome_produto}", {valor})  '
cursor.execute(comando)
conexao.commit()#edita o banco de dados
resultado = cursor.fetchall() #ler o banco de dados

#----------------READ-----------------

comando = f'SELECT * FROM vendas  '
cursor.execute(comando)
resultado = cursor.fetchall() #ler o banco de dados
print(resultado)

#----------------UPDATE-----------------

comando = f'UPDATE vendas SET valor = 10 WHERE nome_produto = "biscoito" '
cursor.execute(comando)
conexao.commit() #editar o banco de dados

#----------------DELETE-----------------

comando = f'DELETE FROM vendas WHERE nome_produto = "biscoito" '
cursor.execute(comando)
conexao.commit() #editar o banco de dados



cursor.close() #Fechar o cursor
conexao.close() #Fechar a conexão



