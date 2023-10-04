
# Ask user to enter a password but there will be conditions, 
# our condition for a valid password is:
# 1. it has to have an upper case
# 2. it has to have a lower case
# If user provides a valid password print 'your password is valid'
# Otherwise, print 'your password is not valid'. 

user_pass = input("Enter a pass. with an upper and lower case:")

# if user_pass equals to user_pass.lower() What do you think? 
# A: it would mean og. consists of all lower cases. 
# if user_pass equals to user_pass.upper(), What do you think? 
# A: it would mean og. consists of all upper cases. 
# Do we want any one of situation above to be true? 
# A: We don't want both of situations above to be false at the 
# same time.

b1 = user_pass != user_pass.lower()
b2 = user_pass != user_pass.upper()

if b1 and b2:
    print("your password is valid")
else:
    print("your password is NOT valid")









