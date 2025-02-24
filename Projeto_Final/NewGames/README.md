## 🗂️ Estrutura do codigo para o projeto final do módulo 15:

```
NewGames/    # Ficheiro principal da base de dados SQLite
├── fork/           
├── master/
├── database/
├── src/
│   ├── create/             # Pasta para criar tabelas na base de dados
│   │   └── create.py       # Script para criar tabelas na base de dados
│   ├── delete/             # Pasta para apagar dados da tabelas na base de dados
│   │   ├── delete.py       # Script para apagar dados da tabelas na base de dados
│   ├── drop/               # Pasta para apagar a tabelas na base de dados
│   │   ├── drop.py         # Script para apagar a tabelas na base de dados
│   ├── insert/             # Pasta para inserir dados a tabelas na base de dados
│   │   ├── insert.py       # Script para inserir dados a tabelas na base de dados
|   ├── select/             # Pasta para consultar dados a tabelas na base de dados
│   │   ├── select.py       # Script para consultar dados a tabelas na base de dados
│   └── update/             # Pasta para atualizar dados a tabelas na base de dados
|       ├── update.py       # Script para atualizar dados a tabelas na base de dados
└── README.md
```

## Gestão da Base de Dados de Jogos
Este projeto utiliza SQLite para gerir informações sobre jogos, incluindo gêneros e plataformas. O código cria e manipula uma base de dados, permitindo a inserção, consulta e exclusão de dados.


## Funcionalidades
### 1. Criação de Tabelas:
- O código cria as seguintes tabelas na base de dados:
    - **jogos**: Armazena informações sobre jogos, como nome, ano, gênero e plataforma;
    - **generos**: Armazena os diferentes gêneros de jogos;
    - **plataformas**: Armazena as plataformas em que os jogos estão disponíveis;

---

### 2. Inserção de Dados
- O código permite inserir dados nas tabelas generos, plataformas e jogos com informações predefinidas, como jogos populares e suas respectivas plataformas e gêneros.

---

### 3. Exclusão de Dados
- É possível excluir jogos específicos ou até mesmo tabelas inteiras (jogos, generos ou plataformas) da base de dados.

---

### 4. Consulta de Dados
- O código realiza consultas combinadas (`INNER JOIN`) entre as tabelas jogos, generos e plataformas para exibir informações sobre jogos, gêneros e plataformas.


## Como Usar

### Pré-requisitos

- Python 3.x
- SQLite3

### 1. Criação da Base de Dados: 
- Ao correr o código `create.py`, as tabelas são criadas automaticamente na base de dados.
### 2. Inserção de Dados: 
- Utilize os comandos dentro do `insert.py` para adicionar jogos, gêneros e plataformas.
### 3. Exclusão de Dados: 
- É possível excluir jogos (`delete.py`) ou tabelas inteiras (`drop.py`).
### 4. Consulta de Dados: 
- Realize consultas com `select.py` para visualizar no terminal os jogos, os gêneros e plataformas.

---

## 🚀 Como Executar

1. Clone ou faça o download deste repositório.
2. Abra o terminal no diretório do projeto.
3. Execute os seguintes arquivos, um de cada vez, para criar as tabelas, inserir os dados, consultar, atualizar e eliminar:

   ```bash
   python create.py
   python insert.py
   python select.py
   python update.py
   python delete.py
   python drop.py


## Observações
- O banco de dados é salvo em um caminho específico no sistema Windows. Altere o caminho conforme necessário. As operações de exclusão são irreversíveis.