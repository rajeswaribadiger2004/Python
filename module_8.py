1.
Program using functions to find greatest of three numbers
def greatest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example
print("Greatest number is:", greatest_of_three(10, 25, 15))

2.
Celsius to Fahrenheit Conversion

Formula: F = (C × 9/5) + 32

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example
print("25°C =", celsius_to_fahrenheit(25), "°F")

3.
Prevent print() from printing a new line

By default, print() adds a newline. Use end="" to prevent it:
print("Hello", end="")
print("World")   # Output: HelloWorld


4.
Recursive function to calculate sum of first n natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)
# Example
print("Sum of first 10 natural numbers:", sum_natural(10))

5.
Print first n lines of the pattern
***  
**  
*  

def pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

# Example
pattern(3)

6.
Convert inches to centimeters

(1 inch = 2.54 cm)

def inches_to_cm(inches):
    return inches * 2.54
# Example
print("10 inches =", inches_to_cm(10), "cm")

7.
Remove a given word from a list and strip it
def remove_word(word_list, word):
    return [w.strip() for w in word_list if w.strip() != word]

# Example
words = [" apple ", " banana", "orange ", "apple"]
print(remove_word(words, "apple"))   # ['banana', 'orange']

8.
Multiplication table of a given number
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# Example
multiplication_table(5)
