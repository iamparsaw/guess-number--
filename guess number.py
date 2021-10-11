print("Choose a number between 1 and 10 to guess")
print("-------------------------------")
userEven = input("is your number even?")
print("-------------------------------")
userMore = input(
    "What is the ratio of your number to 5?--answer with more or less or equal--")
if userMore[0] == "e":
    print("your number is 5")
# number 5
if userMore[0] == "l":
    if userEven[0] == "y":
        user2 = input("is your number 2?")
        if user2[0] == "y":
            print("your number is 2")  # number 2
        elif user2[0] == "n":
            print("your number is 4")  # number 4
    elif userEven[0] == "n":
        user1 = input("is your number 1?")
        if user1[0] == "y":
            print("your number is 1")  # number 1
        elif user1[0] == "n":
            print("your number is 3")  # number 3
if userMore[0] == "m":
    if userEven[0] == "y":
        user6 = input("is your number 6?")
        if user6[0] == "y":
            print("your number is 6")  # number 6
        elif user6[0] == "n":
            print("your number is 8")  # number 8
    elif userEven[0] == "n":
        user7 = input("is your number 7?")
        if user7[0] == "y":
            print("your number is 7")  # number 7
        elif user7[0] == "n":
            print("your number is 9")  # number 9
