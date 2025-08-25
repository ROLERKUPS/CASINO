# LAST UPDATED 25/08/2025 10:51 PM

import random
import os
import time

cash = 500

def menu():
    
    os.system("cls")
    print("Welcome to the casino! | v0.1")
    print("by: ROLERKUPS\n")
    print("1. Slots\n")
    select = int(input("Please select the game you'd like to play! "))
    if select == 1:
        slotrules()
    else:
        print("Invalid Option")
        time.sleep(2)
        menu()

def slotrules():
    
    os.system("cls")
    print("MULTIPLIERS:\n")
    print("Two Sevens = 5x Multiplier")
    print("Two Threes = 3x Multiplier")
    print("Three Sevens = 5x Multiplier, with every dollar you bet adding 0.1 to the multiplier each")
    print("Three Threes = 3x Multiplier, with every dollar you bet adding 0.05 to the multiplier each\n")
    input("PRESS ENTER TO CONTINUE:")
    slot()

def slot():
    
    global cash
    slot1 = random.randint(1, 9)
    slot2 = random.randint(1, 9)
    slot3 = random.randint(1, 9)
    
    os.system("cls")
    bet = input("ENTER YOUR BET AMOUNT: ")
    if bet == "menu":
        os.system("cls")
        menu()
    
    cash -= int(bet)
    multiplier = 5 + (int(bet)/10)
    multiplier2 = 3 + (int(bet)/20)
    
    os.system("cls")
    print(f"${cash}\n")
    print(slot1,slot2,slot3,"\n")

    if slot1 == 7 and slot2 == 7 and slot3 == 7:
        print("well done")
        cash = cash + bet * multiplier
        print("cash: " ,cash)
        input("PRESS ENTER TO CONTINUE: ")
        os.system("cls")
        slot()
    elif slot1 == 7 and slot2 == 7 or slot1 == 7 and slot3 == 7 or slot2 == 7 and slot3== 7:
        print("well done")
        cash = cash + bet * 5
        print("cash: " ,cash)
        input("PRESS ENTER TO CONTINUE: ")
        os.system("cls")
        slot()
    elif slot1 == 3 and slot2 == 3 and slot3 == 3:
        print("well done")
        cash = cash + bet * multiplier2
        print("cash: " ,cash)
        input("PRESS ENTER TO CONTINUE: ")
        os.system("cls")
        slot()
    elif slot1 == 3 and slot2 == 3 or slot1 == 3 and slot3 == 3 or slot2 == 3 and slot3== 3:
        print("well done")
        cash = cash + bet * 5
        print("cash: " ,cash)
        input("PRESS ENTER TO CONTINUE: ")
        os.system("cls")
        slot()
    else:
        print(f"You Lost: ${bet}\n")
        input("PRESS ENTER TO CONTINUE: ")
        os.system("cls")
        slot()
menu()