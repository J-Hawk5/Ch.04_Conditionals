'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
print("Wrestling Trivia")
number_correct = 0
world_champions = int(input("How many wrestling world champions did the US have in 2018?"))
if world_champions == 4:
    print("Correct!")
    number_correct += 1
else:
    print("Incorrect. The answer is 4.")
ncaa_champion = input("What team won the NCAA national team title last year?")
if ncaa_champion == "PSU" or ncaa_champion == "Penn State" or ncaa_champion== "Penn State University"  or ncaa_champion== "psu"  or ncaa_champion =="penn state"  or ncaa_champion =="penn state university":
    print("Correct!")
    number_correct += 1
else:
    print("Incorrect. The answer is Penn State.")

print("A. Southeast Polk")
print("B. Waverly-Shell Rock")
print("C. Ankeny Centennial")
print("D. Waukee")
iowa_hs = input("What school won the 3A team title at this year's wrestling state tournament?")

if iowa_hs.lower() == "b":
    print("Correct!")
    number_correct += 1
else:
    print("Incorrect. The answer was B, Waverly-Shell Rock.")
weight_classes=int(input("How many weight classes are in high school wrestling?"))
if weight_classes == 14:
    print("Correct!")
    number_correct += 1
else:
    print("Incorrect. The answer is 14.")

print("A. Chicago")
print("B. St. Louis")
print("C. Cleveland")
print("D. New York City")
ncaa_tournament=input("Where are next month's NCAA Wrestling championships being held?")

if ncaa_tournament.lower() == "c":
    print("Correct!")
    number_correct += 1
else:
    print("Incorrect. The answer was C, Cleveland.")

print(number_correct, "correct, out of 5")
print(number_correct/5*100, "%")
