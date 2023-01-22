# avengers = ["Iron Man", "Spider Man", "Thor", "Hulk"]
# avengers1 = "Iron Man", "Spider Man", "Thor", "Hulk"
# avengers2 = "Iron Man, Spider Man, Thor, Hulk"
# print(type(avengers))
# print(type(avengers1))
# print(type(avengers2))
# print(len(avengers))
# print(avengers)
# print(type(avengers[0]))
# print(avengers[0])

avengers = []
no_of_avengers = int(input("How many numbers of avengers you want?: "))
for i in range(1, no_of_avengers + 1):
    avengers.append(input("Enter your avengers names: "))
print(avengers)
