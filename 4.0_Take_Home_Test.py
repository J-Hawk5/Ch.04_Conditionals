'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Spencer Daves
'''

# 1. Make the following program work.

midichlorians = float(input("Enter midichlorian count: "))
if midichlorians > 10000:
    print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")

# 2. Make the following program work.

x = input("Enter a number: ")
if x == 3:
    print("You entered 3")

# 3. Make the following program work.

answer = input("What is the name of Poe Dameron's Droid? ")
if answer == "BB8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")

# 4. Make the following program work.

jedi = input("Who are the top 3 greatest Jedi?")
if jedi.lower()=="yoda"or"luke skywalker"or"obi-wan kenobi":
    print("That is correct!")

# 5. Make the following program work whether they enter a, A, Jedi Master or jedi master

print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")
a= "A"
b= "B"
c= "C"
if user_input == a:
    sensitivity = 1000
elif user_input == b:
 sensitivity = 900
else:
    user_input = c
sensitivity = 0
print("Your sensitivity is",sensitivity)