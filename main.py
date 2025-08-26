# LAST UPDATED 26/08/2025 6:10 PM

import random
import os
import time

cash = 500
ring = 1

def broke():

    global ring
    global cash

    if ring == 1:
        os.system("cls")
        print("You get home late from the casino, having lost all your money.")
        time.sleep(2)
        print("Without a second of hesitation you take your grandmother's engagement ring to the casino and pawn it for $450.")
        time.sleep(3)
        print("You head straight back to the casino.")
        time.sleep(2)
        ring = 0
        cash = 450
        slot()
    else:
        print("bro just give up at this point you lose")
        time.sleep(3)
        menu()
        

def menu():
    
    if cash <1:
        broke()
    
    os.system("cls")
    print("Welcome to the casino! | v0.2")
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

    while True:

        if cash < 1:
            print("you broke ass mothafucka get the fuck out")
            time.sleep(3)
            menu()
            return
    
        slot1 = random.randint(1, 9)
        slot2 = random.randint(1, 9)
        slot3 = random.randint(1, 9)
    
        os.system("cls")
     
        bet = input("ENTER YOUR BET AMOUNT: ")
        if bet == "menu":
            os.system("cls")
            menu()
            return
        else:
            try:
                bet = int(bet)
            except ValueError:
                print("Please enter a valid number!")
                time.sleep(2)
                continue
        
        if int(bet) > cash:
            print("You don't have enough money")
            time.sleep(2)
            continue
    
        cash -= int(bet)
        multiplier = 5 + (int(bet)/10)
        multiplier2 = 3 + (int(bet)/20)

        winnings = int(bet) * multiplier
    
        os.system("cls")
        print(f"${cash}\n")
        print(slot1,slot2,slot3,"\n")

        if slot1 == 7 and slot2 == 7 and slot3 == 7:
            print(f"You Won: ${winnings}\n")
            cash = cash + int(bet) * multiplier
            print("cash: " ,cash)
            time.sleep(2)
            os.system("cls")
            continue
        elif slot1 == 7 and slot2 == 7 or slot1 == 7 and slot3 == 7 or slot2 == 7 and slot3== 7:
            print(f"You Won: ${winnings}\n")
            cash = cash + int(bet) * 5
            print("cash: " ,cash)
            time.sleep(2)
            os.system("cls")
            continue
        elif slot1 == 3 and slot2 == 3 and slot3 == 3:
            print(f"You Won: ${winnings}\n")
            cash = cash + int(bet) * multiplier2
            print("cash: " ,cash)
            time.sleep(2)
            os.system("cls")
            continue
        elif slot1 == 3 and slot2 == 3 or slot1 == 3 and slot3 == 3 or slot2 == 3 and slot3== 3:
            print(f"You Won: ${winnings}\n")
            cash = cash + int(bet) * 5
            print("cash: " ,cash)
            time.sleep(2)
            os.system("cls")
            continue
        else:
            print(f"You Lost: ${bet}\n")
            time.sleep(2)
            os.system("cls")
            continue
menu()