print(f'{"*** Programmed by ***": ^40}')
print(f'{"*** Nicolas Fabillar ***": ^40}')

DataList = [" ", " ", " "]
PhoneBook = {
    "Nico" : ["15", "Pampanga", "09223139401"],
    "Duter" : ["17", "Manila", "09211111313"],
    "Ailex" : ["16", "Zamboanga", "09211321313"],
    "Casey" : ["19", "Pangasinan", "09211561323"],
    "Maritez" : ["31", "Bataan", "09212233123"],
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

    if Choice == 2:
        SearchName = input("Enter the full name of the contact: ")
        print("\n===================================== Phone Book =====================================")
        print(f'{"Name": <33} {"Age": <10} {"Address": <33} {"Number": <15}')
        Matches = 0
        for key in PhoneBook:
            if key == SearchName:
                print(f'{key.capitalize(): <33} {PhoneBook[key][0]: <10} {PhoneBook[key][1].capitalize(): <33} {PhoneBook[key][2]: <15}')
                Matches = 1
        if Matches == 0:
            print(f'\n{"*** No match found ***": ^86}')

    if Choice == 3:
        Exit = input("Do you want to exit? y/n: ")
        if Exit == "y":
            print("\n** Program Terminated **")
            exit()
        print("\nCancelled.")