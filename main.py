import math
import time
from config import *
import random
import os

running = True
balance = 1200
pickaxe_durability = 5
upgrade_level = 0
sharpening_cost = 200

inventory = []

# prints everything animated like a typewriter, delays after printing
def typewriter_print(string_to_print):
    for letter in string_to_print:
        print(letter, end="", flush=True)
        time.sleep(0.02)
    print()
    time.sleep(1)

def shop():
    global pickaxe_durability, upgrade_level, balance
    can_upgrade = upgrade_level < len(list(UPGRADE_DICT.items())) - 1
    os.system('clear')
    print("Welcome to the shop!")
    print(f"You have ${balance}")
    print("--------------------")
    print("0) Exit")
    print(f"1) Pickaxe Sharpening\t${sharpening_cost}")
    if can_upgrade:
        print(f"2) {list(UPGRADE_DICT.items())[upgrade_level][0]}\t${list(UPGRADE_DICT.items())[upgrade_level][1]}")
    print("--------------------")
    choice = input("> ")
    if choice == "0":
        main_menu()
        return
    elif choice == "1":
        if balance >= sharpening_cost:
            pickaxe_durability = MAX_DURABILITY
            balance -= sharpening_cost
            typewriter_print("Pickaxe is now on max durability")
            shop()
            return
        else:
            typewriter_print("You don't have enough money!")
            shop()
            return
    elif choice == "2" and can_upgrade:
        if balance >= list(UPGRADE_DICT.items())[upgrade_level][1]:
            balance -= list(UPGRADE_DICT.items())[upgrade_level][1]
            upgrade_level += 1
            typewriter_print("Pickaxe succesfully upgraded!")
            shop()
            return
        else:
            typewriter_print("You don't have enough money!")
            shop()
            return
    else:
        typewriter_print("Invalid choice, please try again.")
        shop()
        return


def view_inventory():
    os.system('clear')
    for item in inventory:
        print(f"{item}\t${ORE_DICT[item]}")
    input("> Press enter to close your inventory...")

def mining():
    global balance, inventory, pickaxe_durability
    os.system('clear')
    if pickaxe_durability <= 0:
        typewriter_print("You cannot mine with a dull pickaxe, go to the shop and sharpen it!")
        input("> Press enter to continue...")
        return
    random_ore = random.choice(list(ORE_DICT.items()))
    random_ore_value = random_ore[1]
    if upgrade_level > 0:
        random_ore_value = math.floor(random_ore_value * (1 + upgrade_level / 10))
    pickaxe_durability -= 1
    print(f"Pickaxe durability: {pickaxe_durability}\\{MAX_DURABILITY}")
    typewriter_print(f"You have found a {random_ore[0]}!")
    print(f"Would you like to sell this ore for ${random_ore_value}? (Y/N)")
    choice = input("> ")
    if choice.lower() == "y":
        balance += random_ore[1]
        typewriter_print(f"You sold the {random_ore[0]}!")
    elif choice.lower() == "n":
        inventory.append(random_ore[0])
        typewriter_print(f"{random_ore[0]} has been added to your inventory!")


def main_menu():
    global running

    os.system('clear')
    print("Main Menu")
    print("----------------")
    print(f"Pickaxe durability: {pickaxe_durability}\\{MAX_DURABILITY}")
    print(f"Wallet: ${balance}")
    if upgrade_level == 0:
        print(f"Pickaxe level: Wooden Pickaxe")
    else:
        print(f"Pickaxe level: {list(UPGRADE_DICT.items())[upgrade_level][0]}")
    print(f"Upgrade level: {upgrade_level}")
    print("----------------")
    print("1) Go mining")
    print("2) Visit the shop")
    print("3) View your inventory")
    print("4) Exit\n")
    choice = input("> ")

    if choice == "1":
        mining()
    elif choice == "2":
        shop()
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        running = False
    else:
        typewriter_print("Invalid choice, please try again.")
        main_menu()
def goodbye():
    os.system('clear')
    typewriter_print("Goodbye, miner!")
    input("> Press enter to exit...")

def intro_scene():
    os.system('clear')
    typewriter_print("Welcome to the mines!")
    typewriter_print("Your job is to get as rich as possible from mining ores and rare artifacts!")
    typewriter_print("You can sell your items and purchase upgrades in the shop.")
    typewriter_print("The pickaxe upgrades modify the amount that you get from selling ores.")
    typewriter_print("Good luck miner!\n")
    input("> Press enter to start the game...")

if __name__ == '__main__':
    intro_scene()
    while running:
        main_menu()
    goodbye()