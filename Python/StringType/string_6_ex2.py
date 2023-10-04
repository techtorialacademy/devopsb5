# Ask user to enter their age, if they enter anything 
# bigger than 2 digit numbers and if they don't enter
# a number print 'invalid age' 
# print "okay"
# Assuming no special characters involved in our machine. 

user_age = input("Enter your age in digits: ")

# What is the data type of user_age? 
# string
# How can we understand if there is more than 2 digit is entered? 
# A: len(user_age)>2 

b1 = 0< len(user_age) <= 2 # We make sure user entered 
# more than 0 and less than equals 2 characters.

# How can i check if the string consists of numbers only? 
# user_age == user_age.upper() 
# user_age == user_age.lower()
b2 = user_age == user_age.upper() and user_age == user_age.lower()

# Think of a string 
# that will be equal to its lower case version.
# tec
# Think of a string 
# that will be equal to its upper case version
# TECH
# Think of a string that would be 
# equal to its lower case version and upper case version 
# at the same time. 
# "22" -> lower case -> "22" -> upper case -> "22"






if b1 and b2:
    print("Your age is:",user_age)
else:
    print("Your age is not valid.")








