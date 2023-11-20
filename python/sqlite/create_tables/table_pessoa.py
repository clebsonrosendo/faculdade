from connection import ConexaoBD as Conexao


try:
    # Execução de comandos
    comando = '''CREATE TABLE Pessoa (
                        cpf INTEGER NOT NULL,
                        nome TEXT NOT NULL,
                        nascimento DATE NOT NULL,
                        oculos BOOLEAN NOT NULL,
                        PRIMARY KEY (cpf)
                        );'''

    openBD = Conexao
    openBD.open(comando)

except:
    print('Erro na criação da tabela')
