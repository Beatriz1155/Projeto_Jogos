import sqlite3

# Conexão com a base de dados
conexao = sqlite3.connect('C:\\Users\\ba2434\\Documents\\Projeto_Final\\NewGames\\master\\database\\exemplo.db')
cursor = conexao.cursor()

# INNER JOIN das três tabelas ao mesmo tempo
query = """
    SELECT j.nome AS Jogo, g.nome AS Genero, p.nome AS Plataforma
    FROM jogos j
    INNER JOIN generos g ON j.genero_id = g.id
    INNER JOIN plataformas p ON j.plataforma_id = p.id;
"""

cursor.execute(query)

# Obter e exibir os resultados
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)  # Cada linha mostra (Jogo, Genero, Plataforma)

# Fechar a conexão
conexao.close()
