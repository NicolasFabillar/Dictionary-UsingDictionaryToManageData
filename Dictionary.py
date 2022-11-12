print(f'{"*** Programmed by ***": ^40}')
print(f'{"*** Nicolas Fabillar ***": ^40}\n')

while True:
    Choice = int(input("\nMenu: \n\t1 -> Add an item \n\t2 -> Search \n\t3 -> Exit (y/n) \nWhat do you want to do? (1-3): "))
    if Choice == 3:
        Exit = input("Do you want to exit? y/n: ")
        if Exit == "y":
            print("\n** Program Terminated **")
            exit()
        print("\nCancelled.")