
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
        
players = ["henrique", "bruno","kelly", "pedro", "andressa"]
print("Here are the first three players on my team")