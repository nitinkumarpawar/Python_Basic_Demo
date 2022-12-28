# file_io = open("myfile.txt", 'w')
# file_io.write("Hello world")
# file_io = open("myfile.txt", "r")
# print(file_io.read())
# for i in file_io.readlines():
# print(file_io.readline())
#     print(i)
# file_io.close()
# w_file = open("read_file.txt", "w")
# w_file.close()
r_file = open("read_file.txt", "r")
wa_file = open("write_file.txt", "a")
for i in r_file.readlines():
    if int(i) % 2 == 0:
        wa_file.write(i)
r_file.close()
wa_file.close()
