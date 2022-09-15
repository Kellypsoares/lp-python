''' 
a função action é a primeira interface com o usuario
ela faz pergunta pela opçoēs e retorne uma string com a opção desejada
'''
agenda = {}

def action(): 
        return input("Digite a opção desejada: (i)incluir, (d)deletar, (b)busca, (s)sair ")

'''' A função incluir cria um registro contendo nome, email e telefone
'''   
def inlcuir():
        print("Incluindo uma pessoa na minha agenda")
        nome = input("digite o nome")
        email = input("Digite o e-mail")
        tel = input("Digite o tel")
        temp = {nome:[email,tel]}
        for nome in temp:
        agenda.update =(temp)

print("Agenda de LP")
a= action()
 

a = input("digite a opção desejada: (i)incluir, (d)deletar, (b)busca, (s)sair ")
while(a!="s"): 
        if(a=="i"): print("incluir")
        elif(a=="d"): print("deleta")
        elif(a=="b"): print("busca aeh")
        elif(a=="s"): print("Obrigada por usar a agenda")
        break   else: print ("Digita direito seu jumento")
 a= 