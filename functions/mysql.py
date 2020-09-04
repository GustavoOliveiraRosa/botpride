import pymysql
import os
PATH_MYSQL = os.environ['SENHA_MYSQL']
print(PATH_MYSQL)

def cmdmysql(cmd):
    # MINHAS PRE DEFINICOES - MYSQL
    conexao = pymysql.connect(db='PRIDE', user='root', passwd=PATH_MYSQL)
    # Cria um cursor:
    cursor = conexao.cursor()
    # Executa o comando:
    cursor.execute(cmd)
    conexao.commit()
    # Recupera o resultado
    resultado = cursor.fetchall()
    # Finaliza a conexao
    conexao.close()
    successs = True
    return resultado