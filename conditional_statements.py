# num = int(input("Enter a number = "))
# # if num > 0:
# #     print("Number is positive")
# # elif num < 0:
# #     print("Number is negative")
# # else:
# #     print("Number is 0")
# if num % 2 == 0 and num > 0:
#     print("Number is even and positive")
# elif num % 2 == 0 and num < 0:
#     print("Number is even and negative")
# elif num % 2 != 0 and num > 0:
#     print("Number is odd and positive")
# else:
#     print("Number is odd and negative")
email = input("Please enter email id: ")
if "@" in email and ((".com" in email) or (".in" in email)):
    print("Valid email id")
else:
    print("Invalid email id")
