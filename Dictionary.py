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
    try:
        Choice = int(input("\nMenu: \n\t1 -> Add an item \n\t2 -> Search \n\t3 -> All Contacts \n\t4 -> Edit Contact "
                       "\n\t5 -> Exit (y/n) \nWhat do you want to do? (1-5): "))
    except ValueError:
        print("\n\tInvalid input, enter an integer.")
    else:
        if Choice == 1:
            while True:
                FullName = input("Enter full name: ")
                Matches = 0
                for key in PhoneBook:
                    if key == FullName:
                        print("Name already exists.\n")
                        Matches = 1
                if Matches == 0:
                    break

            Age = input("Enter age: ")
            Address = input("Enter home address: ")
            Number = input("Enter phone number: ")

            # Putting the inputted data in a List named DataList.
            DataList[0] = Age
            DataList[1] = Address
            DataList[2] = Number

            # Putting the inputted data in a dictionary named PhoneBook with the key being the Full name.
            PhoneBook[FullName] = DataList
            print("Contact added.")

        if Choice == 2:
            SearchName = input("Enter the full name of the contact: ")
            print("\n======================================== All Contacts ========================================")
            print(f'{"Name": <33} {"Age": <10} {"Address": <33} {"Contact Number": <15}')
            Matches = 0
            for key in PhoneBook:
                if key == SearchName:
                    print(f'{key.capitalize(): <33} {PhoneBook[key][0]: <10} {PhoneBook[key][1].capitalize(): <33} {PhoneBook[key][2]: <15}')
                    Matches = 1
            if Matches == 0:
                print(f'\n{"*** No match found ***": ^94}\n')
            print("==============================================================================================")

        if Choice == 3:
            print("\n======================================== All Contacts ========================================")
            print(f'{"Name": <33} {"Age": <10} {"Address": <33} {"Contact Number": <15}')

            for key in PhoneBook:
                print(f'{key.capitalize(): <33} {PhoneBook[key][0]: <10} {PhoneBook[key][1].capitalize(): <33} {PhoneBook[key][2]: <15}')
            print("\n==============================================================================================")

        if Choice == 4:
            ContactName = input("Enter the full name of contact you want to edit: ")
            Matches = 0
            for key in PhoneBook:
                if key == ContactName:
                    print("Match found! ")
                    print("\tName:",key, "\n\tAge:", PhoneBook[key][0],
                          "\n\tAddress:", PhoneBook[key][1].capitalize(), "\n\tContact Number:", PhoneBook[key][2])
                    Matches = 1
                    Change = input("\nDo you want to change this contact? y/n: ")
                    if Change == "y":
                        Age = input("Enter new age: ")
                        Address = input("Enter home address: ")
                        Number = input("Enter phone number: ")
                        DataList[0] = Age
                        DataList[1] = Address
                        DataList[2] = Number
                        del PhoneBook[key]
                        PhoneBook[key] = DataList
                        print("Contact edited.")
                        Matches = 1
                        break

                    if Change == "n":
                        print("\nCancelled.")

            if Matches == 0:
                print("No match found.")

        if Choice == 5:
            Exit = input("Do you want to exit? y/n: ")
            if Exit == "y":
                print("\n** Program Terminated **")
                exit()
            print("\nCancelled.")

        if Choice not in [1,2,3,4,5]:
            print("\n\tInvalid input, out of range.")