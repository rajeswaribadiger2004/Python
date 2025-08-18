1. Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!
2. Write a program to input eight numbers from the user and display all the unique
numbers (once).
3. Can we have a set with 18 (int) and '18' (str) as a value in it?
4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
5. s = {}
What is the type of 's'?
6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.
7. If the names of 2 friends are same; what will happen to the program in problem
6?
8. If languages of two friends are same; what will happen to the program in problem
6?
9. Can you change the values inside a list which is contained in set S?


1.
# Predefined dictionary
dict_hindi = {
    "pustak": "book",
    "kursi": "chair",
    "kutta": "dog",
    "billi": "cat"
}

word = input("Enter the Hindi word to translate: ")
print("Meaning:", dict_hindi.get(word, "Word not found in dictionary"))


2.
numbers = []
for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
unique_numbers = set(numbers)
print("Unique numbers are:", unique_numbers)

3.
Yes. Because 18 (integer) and '18' (string) are different data types.
s = {18, '18'}
print(s)
# Output: {18, '18'}

4.
4. Length of set after adding 20, 20.0 and '20'
s = set()
s.add(20)
s.add(20.0)  # 20 and 20.0 are considered the same in Python
s.add('20')
print("Set:", s)
print("Length of set:", len(s))

5.
Create empty dictionary and add 4 friends’ favorite languages
fav_lang = {}
for i in range(4):
    name = input(f"Enter friend {i+1}'s name: ")
    lang = input(f"Enter {name}'s favorite language: ")
    fav_lang[name] = lang
print("Favorite Languages:", fav_lang)

6.
If languages of 2 friends are same (Problem 6)?
👉 No issue. Values in a dictionary can be duplicate. Example:
{'Ravi': 'Python', 'Sita': 'Python'}

7.
Normally, lists are unhashable and cannot be stored in a set.
Example:
s = { [1,2,3] }   # ❌ Error: unhashable type: 'list'

