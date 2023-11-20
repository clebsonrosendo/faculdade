import sqlite3 as conector


try:

    # Abertura de conexao e aquisição de cursor
    conexao = conector.connect('./db/bdaula.db')
    cursor = conexao.cursor()

    # Execução de comandos
    comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                    VALUES (12345678900, 'João', '2000-01-31', 1)
                    ;'''

    cursor.execute(comando)

    # Efetivação do camando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro", err)

finally:

    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
