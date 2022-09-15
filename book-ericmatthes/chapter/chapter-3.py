fruits = ["banana", "orange", "grape", "apple"]
print(fruits)
fruits = ["banana", "orange", "grape", "apple"]
print(fruits)
fruits[0] = "watermelon"
print(fruits)
message = "My favorite fruit is " + fruits[-1].title() + "."
fruits.append("watermelon")
print(fruits)
print(message)
fruits.insert(0,"banana")
print(fruits)
del fruits[1]
print (fruits)
popped_fruits = fruits.pop()
print (fruits)
print(popped_fruits)
popped_fruits = fruits.pop(3)
print (fruits)
print(popped_fruits)
print(fruits)
too_sweet = "banana"
fruits.remove(too_sweet)
print(fruits)
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)