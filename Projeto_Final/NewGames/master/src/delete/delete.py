import sqlite3

# Conexão com a base de dados
conexao = sqlite3.connect('C:\\Users\\ba2434\\Documents\\Projeto_Final\\NewGames\\master\\database\\exemplo.db')
cursor = conexao.cursor()

# Pedir ao utilizador o nome do jogo a ser apagado
nome_jogo = input("Digite o nome do jogo a ser apagado: ")
cursor.execute("DELETE FROM jogos WHERE nome = ?;", (nome_jogo,))
conexao.commit()  # Guardar as alterações
print(f"Jogo '{nome_jogo}' apagado com sucesso.")

conexao.close()
