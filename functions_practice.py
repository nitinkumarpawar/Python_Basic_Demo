def add(num1, num2):
    print(num1 + num2)


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
add(n1, n2)


def calculate(num1, num2, operation):
    if operation == "+":
        print(int(num1 + num2))
    elif operation == "-":
        print((num1 - num2))
    elif operation == "*":
        print((num1 * num2))
    else:
        print((num1 / num2))


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
opt = input('''
Press + for addition
Press - for subtraction
Press * for multiplication
Press / for division
Enter you choice:
''')

calculate(n1, n2, opt)


def prime_num_or_not(num):
    count = 0
    for n in range(1, num + 1):
        if num % n == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False


print(prime_num_or_not(10))

encript = int(input("Please enter a prime number to build an encription key: "))
if prime_num_or_not(encript):
    print("You can build an encription key")
else:
    print("Prime number required to build an encription key")
