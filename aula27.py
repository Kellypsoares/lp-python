import sqlite3
conn = sqlite3.connect('pd.db')
c = conn.cursor() #cursor é um ponteiro pra aquele arquivo 

a = input("Me diga seu DRE:")
b = input("Me diga seu nome:")
#'''é um comando quando estiver entre parentesis, string de multiplas linhas
c.execute(" INSERT INTO alunos VALUES (' "+a+" ',' "+b+" ')")

j = c.execute( "SELECT + FROM alunos").fetchall()

#c.execute(''' CREATE TABLE IF NOT EXISTE alunos[dre] interger PRIMARY KEY, [nota1]) INTEGER, [nota2] INTEGER ''')
conn.commit()

c.execute (DELETE from alunos where nome = '"+a+"'")
#"DELETE from alunos where nome = ?, (a,)"

print(j)
