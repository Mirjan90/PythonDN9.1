
print("Welcome user! This program converts you from kilometers to miles.")

while True:
    km = int(input("Please write number of kilometers that you want to convert: "))

    miles = km * 0.621371192

    print("Miles are: " + str(miles))

    choose = input("Do you want to do another conversion? (y/n): ")

    if choose == "n":
        print("Thank you and goodbye!")
        break