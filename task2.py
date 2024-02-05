# 2. *Password Generator:* Develop a program that can generate secure passwords 
# using a combination of letters, numbers, and symbols. Allow users to specify the 
# desired length and complexity of the password.

print("*Password Generator:*")
import random
import string
print("welcome to passsword genrator!!")
password_length=eval(input("enter a password length:"))
character=string.ascii_letters + string.digits + string.punctuation
password=""
for index in range(password_length):
    password=password+random.choice(character)
print("password genratotr:",password)


 
