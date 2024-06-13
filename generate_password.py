import random

print("\n***WELCOME TO THE PASSWORD GENERATOR***\n")
print("The Generated password must contain atleast One 'UPPER CASE' , 'lower case' , 'special character' , and a 'number'. ")
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_chars = "!@#$%^&*()?><~_(){}[]\|/"

all = upper_letters+lower_letters+numbers+special_chars
length_password = int(input("Enter the length of the password ?: "))
password = "".join(random.sample(all,length_password))

print("\nYour password is generated Succesfully...\n    ",password)
