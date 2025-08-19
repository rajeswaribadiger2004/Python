# Program to find the greatest of four numbers (without max)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

# First compare a and b
if a > b:
    greatest1 = a
else:
    greatest1 = b

# Compare greatest1 with c
if greatest1 > c:
    greatest2 = greatest1
else:
    greatest2 = c

# Finally compare with d
if greatest2 > d:
    greatest = greatest2
else:
    greatest = d

print("The greatest number is:", greatest)


2.)
# Program to check if student passed or failed
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

total_percentage = (m1 + m2 + m3) / 3

if total_percentage >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33:
    print("Pass")
else:
    print("Fail")

3.
# Program to detect spam comments
comment = input("Enter your comment: ").lower()

spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

is_spam = False
for word in spam_keywords:
    if word in comment:
        is_spam = True
        break

if is_spam:
    print("This is a spam comment!")
else:
    print("This is not a spam comment.")

4.
# Program to check username length
username = input("Enter your username: ")

if len(username) < 10:
    print("Username contains less than 10 characters.")
else:
    print("Username is valid (10 or more characters).")

4.
# Program to check if name is present in list
names = ["Ramesh", "Suresh", "Rajesh", "Anita", "Priya"]

user_name = input("Enter a name to check: ")

if user_name in names:
    print(user_name, "is present in the list.")
else:
    print(user_name, "is not present in the list.")

5.
# Program to check if name is present in list
names = ["Ramesh", "Suresh", "Rajesh", "Anita", "Priya"]

user_name = input("Enter a name to check: ")

if user_name in names:
    print(user_name, "is present in the list.")
else:
    print(user_name, "is not present in the list.")

6.
# Program to calculate grade
marks = int(input("Enter your marks (0-100): "))

if 90 <= marks <= 100:
    grade = "Ex"
elif 80 <= marks < 90:
    grade = "A"
elif 70 <= marks < 80:
    grade = "B"
elif 60 <= marks < 70:
    grade = "C"
elif 50 <= marks < 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

7.# Program to check if post talks about Harry
post = input("Enter your post: ").lower()

if "harry" in post:
    print("This post is talking about Harry.")
else:
    print("This post is not talking about Harry.")
