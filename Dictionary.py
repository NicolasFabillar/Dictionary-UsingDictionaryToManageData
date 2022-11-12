print(f'{"*** Programmed by ***": ^40}')
print(f'{"*** Nicolas Fabillar ***": ^40}\n')

DataList = [" ", " ", " "]
PhoneBook = {

}

while True:
    Choice = int(input("\nMenu: \n\t1 -> Add an item \n\t2 -> Search \n\t3 -> Exit (y/n) \nWhat do you want to do? (1-3): "))
    if Choice == 1:
        FullName = input("Enter your full name: ")
        Age = input("Enter your age: ")
        Address = input("Enter your home address: ")
        Number = input("Enter your phone number: ")

        # Putting the inputted data in a List named DataList.
        DataList[0] = Age
        DataList[1] = Address
        DataList[2] = Number

        # Putting the inputted data in a dictionary named PhoneBook with the key being the Full name.
        PhoneBook[FullName] = DataList
        print("Contact added.")

        # For testing.
        for key in PhoneBook:
            print(key, PhoneBook[key])


    if Choice == 3:
        Exit = input("Do you want to exit? y/n: ")
        if Exit == "y":
            print("\n** Program Terminated **")
            exit()
        print("\nCancelled.")