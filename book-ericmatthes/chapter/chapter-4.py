
teachers = ["xandão", "regina", "aline","ronaldo"]
for teacher in teachers: 
        print(teacher.title() + ", thank you for all!")        
        print("I can't wait to see you again, " + teacher.title() + ".\n")
print("You are the best")



for value in range(1,5):
        print(value)

numbers = list(range(1,5))
print(numbers)
even_numbers = list(range(2,11,3))
print(even_numbers)

squares = []
for value in range(1,11): 
        square = value**2
        squares.append(square)
        print(squares)

squares = []
for value in range(1,11): 
        squares.append(value**2)
        print(squares)
 #Uma list comprehension (abrangência de lista) permite gerar essa mesma lista com apenas uma linha de código. Uma list comprehension combina o laço for e a criação de novos elementos em uma linha, e concatena cada novo elemento automaticamente.       
squares = [value**2 for value in range(1,11)]
print(squares)


#metódo pra encontrar o valor mínimo, máximo e o somatório de uma lista

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits)) 
print(max(digits))
print(sum(digits))


#Para criar uma fatia, especifique o índice do primeiro e do último elemento 
# ...com os quais você quer trabalhar. 
# ...Como ocorre na função range(), Python para em um item
# ...antes do segundo índice que você especificar. 
# ...Para exibir os três primeiros elementos de uma lista, 
# ...solicite os índices de 0 a 3; os elementos 0, 1 e 2 serão devolvidos.
students = ["henrique", "bruno","kelly", "pedro", "andressa"]
print(students[0:3])
print("Here are the first three players on my team")

#Se o primeiro índice de uma fatia for omitido, 
#...Python começará sua fatia automaticamente no início da lista:

print(students [:4])
# o oposto também é verdade 
print(students[2:])

#um índice negativo devolve um elemento a uma 
#...determinada distância do final de uma lista
print(students[-3:])

#Percorrendo uma fatia com um laço

students = ["henrique", "bruno","kelly", "pedro", "andressa"]
print("Here are the first three students on my class")
for student in students[0:3]:
        print(student.title())

