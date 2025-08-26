# LAST UPDATED 26/08/2025 9:21 PM

import random
import os
import time

cash = 500
ring = True
loan = True

def gamble(bet):

    global cash

    x = bet // 2
    os.system("cls")
    print(f"You have ${x} to gamble.")
    while x > 0:
        print("Choose your gamble:\n")
        print("1 - 50/50 gamble (win = 2x your money)")
        print("2 - 25 percent gamble (win = 4x your money)")
        print("3 - Cash out and keep your winnings!\n")

        choice = input("Enter '1', '2', or '3': ")

        if choice == "1":
            guess = input("Pick 1 or 2: ")
            outcome = str(random.randint(1,2))
            if guess == outcome:
                x *= 2
                print(f"You won! Your gambling money is now ${x}")
                time.sleep(2)
                os.system("cls")
            else:
                print("You lost your gambling money!")
                time.sleep(2)
                os.system("cls")
                x = 0
        elif choice == "2":
            guess = input("Pick a number between 1 and 4: ")
            outcome = str(random.randint(1,4))
            if guess == outcome:
                x *= 4
                print(f"You won! Your gambling money is now ${x}")
                time.sleep(2)
                os.system("cls")
            else:
                print("You lost your gambling money!")
                time.sleep(2)
                os.system("cls")
                x = 0
        elif choice == "3":
            print(f"You cashed out with ${x}")
            time.sleep(2)
            os.system("cls")
            cash = cash + x
            return slot()
        else:
            print("Invalid Choice.")
            time.sleep(2)
            os.system("cls")

def broke():

    global ring
    global cash
    global loan

    if ring == True:
        os.system("cls")
        print("You get home late from the casino, having lost all your money.")
        time.sleep(2)
        print("Without a second of hesitation you take your grandmother's engagement ring and pawn it for $450.")
        time.sleep(3)
        print("You head straight back to the casino.")
        time.sleep(2)
        ring = False
        cash = 450
        slot()
    elif loan == True:
        os.system("cls")
        print("With nowhere left to turn, you set up a meet with one of the city's cruelest loan sharks.")
        time.sleep(3)
        print("The man agrees to give you $500, with the agreement you'll pay him back $1000 in five days.")
        time.sleep(3)
        print("You head straight back to the casino.")
        time.sleep(3)
        loan = False
        cash = 500
        slot()
    else:
        os.system("cls")
        print("You walk yourself home from the casino, late at night, pockets empty, and the smell of alcohol repulsing those around you.")
        time.sleep(3)
        print("You turn the corner to find the loan shark waiting for you, with a few of his goons. You won't be getting out of this one.")
        time.sleep(3)
        print("Everything goes dark.")
        time.sleep(3)
        os.system("cls")
        time.sleep(999999)
        menu()
        
def menu():
    
    if cash <1:
        broke()
    
    os.system("cls")
    print("Welcome to the casino! | v0.1.3")
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
    print("JACKPOT NUMBERS: 3 7\n")
    print("Two Sevens = 5x Multiplier")
    print("Two Threes = 3x Multiplier")
    print("Three Sevens = 5x Multiplier, with every dollar you bet adding 0.1 to the multiplier each")
    print("Three Threes = 3x Multiplier, with every dollar you bet adding 0.05 to the multiplier each\n")
    print("LUCKY NUMBERS: 1 5 9\n")
    print("If you get two or more numbers in the same spin, you get the option to gamble your money.")
    print("You can either take a 50 percent bet which doubles your money, or a 25 percent bet which quadruples your money.\n")
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

        print(f"${cash}")
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
    
        os.system("cls")
        print(f"${cash}\n")
        print(slot1,slot2,slot3,"\n")

        if slot1 == 7 and slot2 == 7 and slot3 == 7:
            winnings = int(bet) * multiplier
            print(f"You Won: ${winnings}\n")
            cash = cash + winnings
            print("cash: " ,cash)
            time.sleep(2)
            os.system("cls")
            continue
        elif slot1 == 7 and slot2 == 7 or slot1 == 7 and slot3 == 7 or slot2 == 7 and slot3== 7:
            winnings = int(bet) * 5
            print(f"You Won: ${winnings}\n")
            cash = cash + winnings
            print("cash: " ,cash)
            time.sleep(2)
            os.system("cls")
            continue
        elif slot1 == 3 and slot2 == 3 and slot3 == 3:
            winnings = int(bet) * multiplier2
            print(f"You Won: ${winnings}\n")
            cash = cash + winnings
            print("cash: " ,cash)
            time.sleep(2)
            os.system("cls")
            continue
        elif slot1 == 3 and slot2 == 3 or slot1 == 3 and slot3 == 3 or slot2 == 3 and slot3== 3:
            winnings = int(bet) * 3
            print(f"You Won: ${winnings}\n")
            cash = cash + winnings
            print("cash: " ,cash)
            time.sleep(2)
            os.system("cls")
            continue
        elif (slot1 == slot2 or slot2== slot3 or slot1 == slot3) and (slot1 in [1,5,9] or slot2 in [1,5,9] or slot3 in [1,5,9]):
            print("You matched two lucky numbers! Time to gamble!")
            time.sleep(2)
            gamble(bet)
        else:
            print(f"You Lost: ${bet}\n")
            time.sleep(2)
            os.system("cls")
            continue
os.system("title CASINO")
menu()