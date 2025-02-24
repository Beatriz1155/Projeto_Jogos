import sqlite3

conexao = sqlite3.connect('C:\\Users\\ba2434\\Documents\\Projeto_Final\\NewGames\\master\\database\\exemplo.db')
cursor = conexao.cursor()

cursor.execute('''
               INSERT INTO generos (nome) 
               VALUES 
               ("RPG"),
               ("FPS"),
               ("Ritmo"), 
               ("Sobrevivência e Ação"), 
               ("Exploração"),
               ("Quebra-cabeça")
               ''')

#------------------------------------------------------------------------------------------------------------

cursor.execute('''
               INSERT INTO plataformas (nome)
               VALUES 
               ("PC"),
               ("Nintendo"),
               ("PlayStation"),
               ("Xbox"),
               ("Arcade"),
               ("Mobile")
               ''') 

#------------------------------------------------------------------------------------------------------------

cursor.execute('''
               INSERT INTO jogos (nome, ano, genero_id, plataforma_id) 
               VALUES 
               ("Valorant", 2020, 2, 1),
               ("MaiMai", 2012, 3, 5),
               ("Hogwarts Legacy", 2023, 6, 3),
               ("Minecraft", 2009, 4, 1),
               ("Hollow Knight", 2017, 4, 4),
               ("Grand Summoners", 2016, 1, 6)
               ''')

#------------------------------------------------------------------------------------------------------------~´

conexao.commit() #Guarda as alterações
conexao.close()