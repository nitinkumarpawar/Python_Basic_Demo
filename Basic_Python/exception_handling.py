def log(msg):
    file = open("error.log", "a")
    file.write(msg+"\n")
    file.close()

try:
    num = int(input("Enter the number: "))
    for i in range(1, num+1):
        if i % 2 == 0:
            print(str("Even number: ") + str(i))
except NameError as e:
    log(str(e))
    print("This is NameError")
except ValueError as e:
    log(str(e))
    print("Invalid value as input")
except Exception as e:
    try:
        log(str(e))
        print("Some error")
    except Exception as e:
        print("Some error while logging error")
finally:
    print("End of the code")