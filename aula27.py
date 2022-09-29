import sqlite3
conn = sqlite3.connect('pd.db')
c = conn.cursor()
#'''é um comando quando estiver entre parentesis, string de multiplas linhas
c.execute(''' CREATE TABLE IF NOT EXISTE alunos[dre] interger PRIMARY KEY, [nota1]) INTEGER, [nota2] INTEGER ''')
conn.commit()