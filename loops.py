email = input("Please enter email id: ")
while True:
    if ("@" in email) and ((".com" in email) or (".in" in email)):
        print("Valid email id")
        break
    else:
        print("Invalid email id")
        email = input("Please enter again: ")
