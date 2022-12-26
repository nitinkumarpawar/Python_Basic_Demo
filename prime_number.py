num = int(input("Please enter a number: "))
count = 0
for n in range(1, num + 1):
    if num % n == 0:
        count += 1
if count == 2:
    print(str(num) + " is a prime number")
else:
    print(str(num) + " is not a prime number")
