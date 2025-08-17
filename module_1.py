1. Write a program to print Twinkle twinkle little star poem in python. 
2. Use REPL and print the table of 5 using it.  
3. Install an external module and use it to perform an operation of your interest.  
4. Write a python program to print the contents of a directory using the os module. 
Search online for the function which does that.  
5. Label the program written in problem 4 with comments. 


1.
print("Twinkle, twinkle, little star,")
print("How I wonder what you are!")
print("Up above the world so high,")
print("Like a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("How I wonder what you are!")

2.
for i in range(1, 11):
  print(f"5 x {i} = {5*i}")

3.
import pyjokes

joke = pyjokes.get_joke()
print(joke)

4.
import os
# Path of the directory
directory_path = "."
# Print the contents of the directory
contents = os.listdir(directory_path)
print("Directory contents are:", contents)
