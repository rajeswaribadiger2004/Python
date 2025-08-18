1. Write a python program to display a user entered name followed by Good
Afternoon using input () function.
2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
3. Write a program to detect double space in a string.
4. Replace the double space from problem 3 with single spaces.
5. Write a program to format the following letter using escape sequence
characters.

1.
name = input("Enter your name: ")
print("Good Afternoon,", name)

2.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
name = input("Enter your name: ")
date = input("Enter date: ")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)

3.
text = "This is  a string with  double spaces."
if "  " in text:
    print("Double spaces detected.")
else:
    print("No double spaces found.")

4.
text = "This is  a string with  double spaces."
new_text = text.replace("  ", " ")
print("Before:", text)
print("After:", new_text)

5.
letter = "Dear Harry,\n\tThis Python course is nice.\nThanks!"
print(letter)

