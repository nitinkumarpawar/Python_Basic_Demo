def log(msg):
    file = open("./error.log","a")
    file.write(msg+"\n")
    file.close()

try:
    for i in range(1, 11):
        if i % 2 == 0:
            print(str("Even number: ") + str(i))
except Exception as e:
    log(str(e))
    print("Some error")
finally:
    print("End of the code")