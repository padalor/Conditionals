'''
For this assignment you should read the task, then below the task do what it asks you to do.
'''

'''
#1) Create a Variable called grade and set it to an integer. Make an if statement that checks if the grade is a passing grade. grade must be above 65 to pass. print out "student is passing"
'''
grade = 75 
if grade > 65:
    print("student is passing")
'''
#2) Now make an if, else statement that checks if the student is passing but also print "student is failing", if the grade is less than 65
'''
if grade > 65:
    print("student is passing")
else:
    print("student is failing")
'''
#3)Create a variable called age. Make and if, else statement that checks if the age entered is old enough to vote. Remember the voting age is 18
'''
age = 17
if age > 17:
    print("old enough to vote")
else:
    print("not old enough")
'''
#4)Create a variable called weight. Make an if statement that checks the unit of the weight. If the weight is in kilograms, convert it to pounds 
'''
weight = 130
if type(weight) == int:
    print(weight*0.45359)
'''
#5)Now modify the previous program to also convert from pounds to kilograms
'''
weight = 85
if type(weight) == int:
    print(weight/0.45359)
'''
#6)create a list (seat1 = 1, seat2 = 1, seat3 = 0, seat4 = 1), Now make an if elseif, else statement that checks if a seat is open. if the seat = 1 its closed and print that it's closed. If the seat = 0, it's open and print that it's open. If no seats are open print "There are no available seats"
'''
seat = [1, 1, 0, 1]
if seat == 1:
    print("seat is open")
elif seat == 0:
    print("seat is closed")
else:
    print("There are no available seats")


