# num = int(input("Please enter the number: "))
#count = 0
# for n in range(1, num+1):
#     if num % n == 0:
#         count += 1
# if count == 2:
#     print("Entered number " + str(num) + " is a prime number")
# else:
#     print("Entered number " + str(num) + " is not prime nymber")
for num in range(1, 101):
    count = 0
    for n in range(1, num+1):
        if num % n == 0:
            count += 1
    if count == 2:
        print("Entered number " + str(num) + " is a prime number")
