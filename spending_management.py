# spending management

import datetime

def input_cost():
    while True:
        try:
            cost = int(input("Item cost (USD): "))
            while cost > 0:
                return cost
                break
            else:
                print("Let buy something\n")
        except ValueError:
            print("Invalid input. Try again")
            print()

def choose_option():
    print("""What do you want to do? \n
    1. Add item\n
    2. Remove item\n""")
    while True:
        try:
            option = int(input("Select option 1 or 2: "))
            if 1 <= option <= 2:
                return option
                break
            else:
                print("You only have 2 options. Try again\n")
        except ValueError:
            print("Invalid input. Try again")

def add_item(temp_list, item):
    temp_list.append(item)

def remove_item(temp_list, name):
    count = 0
    for i in range(len(temp_list) - 1, -1, -1):
        if temp_list[i]["name"].lower() == name.lower():
            count += 1
            temp_list.pop(i)
    if count == 0:
        print("\n------------------------------------------")
        print(f"{name.capitalize()} is not in your expenses")
        print("------------------------------------------\n")

def try_again():
    choice = input("Do you want to try more? (Y/N): ").upper().strip()
    if choice == "Y" or choice == "YES":
        return True
    else:
        print("Bye! See you next time!")
        exit()

def print_list(list):
    for i in range(len(list)):
        print(list[i])

if __name__ == '__main__':
    expenses = [{'name': 'Car', 'cost': 130, 'date': '08/27/21 22:39:28'},
                {'name': 'car', 'cost': 15000, 'date': '08/27/21 23:05:59'},
                {'name': 'pen', 'cost': 5, 'date': '08/27/21 23:06:08'},
                {'name': 'pen', 'cost': 3, 'date': '08/27/21 23:06:19'}]
    #print(expenses)
    while True:
        option = choose_option()
        name_input = input("Item name: ")
        if option == 1:
            cost_input = input_cost()
            date_input = datetime.datetime.now().strftime("%x %X")
            item = {"name": name_input,
                    "cost": cost_input,
                    "date": date_input}
            add_item(expenses, item)
            print("Your expenses: ")
            print_list(expenses)
            print()
        else:
            remove_item(expenses, name_input)
            print("Your expenses: \n")
            print_list(expenses)
            print()
        try_again()