#The program checks if a name is more than 3 characters long, any name that has less than 4 characters is invalid.
#It takes the name as input, and raises an exception if the name is invalid, outputting "Invalid Name". Outputs "Account Created" if the name is valid.
try:
    name = input()
    if len(name)>3:
        print("Account Created")
    else:
        raise NameError
except:
    print("Invalid Name")
