1. Write a program to store seven fruits in a list entered by the user.
2. Write a program to accept marks of 6 students and display them in a sorted
manner.
3. Check that a tuple type cannot be changed in python.
4. Write a program to sum a list with 4 numbers.
5. Write a program to count the number of zeros in the following tuple:


1.
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)
print("Fruits list:", fruits)


2.
marks = []
for i in range(6):
    mark = int(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)
print("Original marks:", marks)
marks.sort()
print("Sorted marks:", marks)


3.
t = (1, 2, 3, 4)
print("Original tuple:", t)
try:
    t[1] = 99
except TypeError as e:
    print("Error:", e)
    print("This proves tuple is immutable.")

4.
numbers = []
for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
print("Numbers:", numbers)
print("Sum of numbers:", total)

5.
t = (7, 0, 8, 0, 0, 9, 0)
count = t.count(0)
print("Tuple:", t)
print("Number of zeros:", count)


NOTE
A list is a collection of ordered and mutable (changeable) elements.
Syntax: Written with square brackets [].

A tuple is a collection of ordered and immutable (unchangeable) elements.
Syntax: Written with parentheses ().

A dictionary is a collection of key–value pairs, unordered, and mutable.
Syntax: Written with curly braces {} and keys with values separated by :
