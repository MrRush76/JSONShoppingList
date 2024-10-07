import time as t
import json
with open('file.json') as json_file:
    shopping_list = json.load(json_file)
def menu(shopping_list):
    while True:
        print("1. Add to list")
        print("2. Remove from list")
        print("3. Update quantity")
        print("4. View shopping list")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            shopping_list = AddToList(shopping_list, input("Enter the item: "), int(input("Enter the quantity: ")))
            ViewShoppingList(shopping_list)
            with open("file.json", "w") as fp:
                json.dump(shopping_list, fp)
            t.sleep(2)
        elif choice == 2:
            shopping_list = RemoveFromList(shopping_list, input("Enter the item: "))
            ViewShoppingList(shopping_list)
            with open("file.json", "w") as fp:
                json.dump(shopping_list, fp)
            t.sleep(2)
        elif choice == 3:
            shopping_list = UpdateQuantity(shopping_list, input("Enter the item: "), int(input("Enter the new quantity: ")))
            ViewShoppingList(shopping_list)
            with open("file.json", "w") as fp:
                json.dump(shopping_list, fp)
            t.sleep(2)
        elif choice == 4:
            ViewShoppingList(shopping_list)
            if len(shopping_list) == 0:
                print("The shopping list is empty")
            t.sleep(2)
        else:
            break
def AddToList(sList, item, amount):
    if amount > 0:
        sList[item] = amount
        return sList
    else:
        print("Invalid quantity")
        return sList

def RemoveFromList(sList, item):
    if item in sList:
        del sList[item]
        return sList
    else:
        print("Item not found in list")
        return sList


def UpdateQuantity(sList, item, newQuanity):
    if newQuanity > 0:
        sList[item] = newQuanity
        return sList
    else:
        print("Invalid quantity")
        return sList
def ViewShoppingList(sList):
    for item in sList:
        print(item, sList[item])

menu(shopping_list)





















# def pythagoras(a, b):
#     c = ((a**2) + (b**2))**0.5
#     return c
#
#
# side_1 = float(input("Enter the length of the first side: "))
# side_2 = float(input("Enter the length of the second side: "))
# hypotenuse = pythagoras(side_1, side_2)
# print("The value of c is: ", hypotenuse)
