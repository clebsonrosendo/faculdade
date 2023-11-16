import sqlite3 as conector

try:

    # Abertura de conexao e aquisição de cursor
    conexao = conector.connect('./db/bdaula.db')
    cursor = conexao.cursor()

    print('Conexão Bem-sucedida')

    try:
        # Execução de comandos
        comando = '''CREATE TABLE Pessoa (
                            cpf INTEGER NOT NULL,
                            nome TEXT NOT NULL,
                            nascimento DATE NOT NULL,
                            oculos BOOLEAN NOT NULL,
                            PRIMARY KEY (cpf)
                            );'''

        cursor.execute(comando)

        # Efetivação do camando
        conexao.commit()

        print('Tabela Pessoa criada')

    except conector.OperationalError as err:
        print('Erro na criação da tabela', err)


except conector.DatabaseError as err:
    print('Erro no banco de dados', err)


finally:

    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
