import sqlite3

conexao = sqlite3.connect('C:\\Users\\ba2434\\Documents\\Projeto_Final\\NewGames\\master\\database\\exemplo.db') #Conexão com a DataBase
cursor = conexao.cursor()

#Criação da tabela mecanicos com os valores id_mecanicos, nome e idade
cursor.execute('''
    CREATE TABLE IF NOT EXISTS jogos (  
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        genero_id INTEGER NOT NULL,
        plataforma_id INTEGER NOT NULL,
        FOREIGN KEY (genero_id) REFERENCES genero(id),
        FOREIGN KEY (plataforma_id) REFERENCES plataformas(id)
    );
''')

#Criação da tabela serviços com os valores id, carro e mecanicos_id (que faz referencia a id_mecanicos)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS generos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS plataformas (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL
    );
''')

conexao.commit() #Guarda as alterações
conexao.close()