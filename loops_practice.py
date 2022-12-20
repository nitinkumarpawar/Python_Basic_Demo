# count = 1
# while count <= 5:
#     print(count)
#     count += 1
# for count in range(1, 11, 3):
#     print(count)
data = input("Enter the string: ")
count = 0
for character in data:
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
        count += 1
print("Vovels in "+data+" are " + str(count))
