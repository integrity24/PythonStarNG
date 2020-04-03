import random
import string

def randomString(stringLength = 5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

first_name = input("First Name: ")
last_name = input("Last Name: ")
email = input("Email Address: ")
password = first_name[0] + first_name[1] + last_name[-2] + last_name[-1]
password = password + randomString()
print(password)
condition = input ("Do you like the password, input yes or no: ")
if condition == "yes":
    print("This is your password" + " " + password)
elif condition == "no":
    new_password = input("Enter your desire password: ")
    if len(new_password) >= 7:
        password = new_password
    else:
        input("Enter a seven letter password: ")
        pass

print(first_name)
print(last_name)
print(password)