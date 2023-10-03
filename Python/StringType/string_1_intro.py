# Ask user to enter a string 
# print the length of the given string, and print the 
# 5th letter from string. 

s = input("Enter anything:")

#What is the length for this string? 
print(len(s))

# What would be the last(biggest) index number in string above? 
biggest_index = len(s) - 1
if biggest_index >= 4:
    print(s[4])
else: 
    print("Sorry, but there is no index 4 in string.")

 



# Refactor this code so that it wouldn't generate an error when
# user enters a string that doesn't have index 4. 












# Note! If the index number we are trying to access doesn't 
# exist in string, it will generate IndexError. 









