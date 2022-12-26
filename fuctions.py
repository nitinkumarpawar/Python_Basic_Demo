def validate_email_id(email_to_validate):
    while True:
        if ("@" in email_to_validate) and ((".com" in email_to_validate) or (".in" in email_to_validate)):
            print("Valid email id")
            break
        else:
            print("Invalid email id")
            break


email1 = input("Enter email id: ")
validate_email_id(email1)
