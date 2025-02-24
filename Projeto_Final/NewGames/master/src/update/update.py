import sqlite3

conexao = sqlite3.connect('C:\\Users\\ba2434\\Documents\\Projeto_Final\\NewGames\\master\\database\\exemplo.db') #Conexão com a DataBase
cursor = conexao.cursor()

cursor.execute('UPDATE jogos SET plataforma_id = 3 WHERE plataforma_id = 5')
cursor.execute('UPDATE jogos SET genero_id = 2 WHERE genero_id = 1')
conexao.commit() #Guarda as alterações
conexao.close() #Fechar conexãos