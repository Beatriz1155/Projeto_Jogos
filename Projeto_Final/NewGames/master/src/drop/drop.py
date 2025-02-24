import sqlite3

# Solicitar ao utilizador o nome da tabela a ser apagada
tabela = input("Digite o nome da tabela que deseja apagar: ")

# Verificar se o nome da tabela é válido
tabelas_validas = ['jogos', 'genero_id', ' plataforma_id']
if tabela not in tabelas_validas:
    print(f"A tabela '{tabela}' não é válida ou não existe.")
else:
    # Conectar ao banco de dados
    with sqlite3.connect('C:\\Users\\ba2434\\Documents\\Projeto_Final\\NewGames\\master\\database\\exemplo.db') as conexao:
        cursor = conexao.cursor()

        # Apagar a tabela especificada
        cursor.execute(f"DROP TABLE IF EXISTS {tabela};")

        conexao.commit()  # Salvar as alterações

    print(f"Tabela '{tabela}' apagada com sucesso.")
