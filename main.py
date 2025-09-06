# LAST UPDATED 6/09/2025 8:57 PM

import random
import os
import time
import threading

start_time = time.time()
days_passed = 0
day_length = 180
ATK = 0
knife = False
poo = False
shark_tracking = -1

cash = 500
ring = True
loan = True
slot_rules_shown = False 

def track_days():
    global days_passed
    global shark_tracking

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= (days_passed + 1) * 180:
            days_passed += 1
            os.system("cls")
            print("You decide it's too late and time to call it a night.")
            print(f"DAY: {days_passed}")
            time.sleep(3)
            if poo and days_passed >= shark_tracking + 5:
                    loan_shark_event()
                    shark_tracking = days_passed
                    return_to_game()
        time.sleep(1)

def loan_shark_event():
    global shark_tracking, knife, poo, cash, ring, loan, ATK
    while True:
        os.system("cls")
        print("Five days have passed, and as you leave the casino the loan shark drags you into a nearby alley, knife in hand.")
        time.sleep(4)
        print("The man furiously demands the payment of $1000 you owe him")
        time.sleep(3)
        if cash > 1000:
            print("What do you decide to?\n")
            print("1. Pay him the $1000")
            print("2. Refuse to pay him (fight)")
            print("3. Attempt to negotiate paying him more later")
            loan_shark_selection = int(input("SELECT EITHER '1', '2', OR '3': "))
            if loan_shark_selection == 1:
                os.system("cls")
                cash -= 1000
                print("You pay the man, and he leaves in a hurry.")
                return_to_game()
                return
            elif loan_shark_selection == 2:
                os.system("cls")
                fight_chance = random.randint(1,100)
                if fight_chance <= 10 + ATK:
                    print ("You managed to knock him out. You take his stuff.\n")
                    print("CASH: +1000")
                    cash += 1000
                    print("ITEM: +KNIFE")
                    knife = True
                    return_to_game()
                    return
            elif loan_shark_selection == 3:
                os.system("cls")
                print("You try to run, but the man is blocking the exit.")
                time.sleep(2)
                return
        else:
            print("You don't have enough money to pay the man back.")
            time.sleep(2)
            print("What do you decide to do?\n")
            print("1. Attempt to negotiate a deal")
            print("2. Refuse to pay him (fight)")
            loan_shark_selection2 = int(input("SELECT EITHER '1', OR '2': "))
            if loan_shark_selection2 == 1:
                negotiate_chance = random.randint(1,100)
                if negotiate_chance <= 50:
                    print("The loan shark beats you badly, and says you have one more day to pay $2000")
                    time.sleep(2)
                    return_to_game()
                    return
                else:
                    print("The loan shark stabs you, and everything goes dark.")
                    exit()
            elif loan_shark_selection2 == 2:
                os.system("cls")
                fight_chance = random.randint(1,100)
                if fight_chance <= 10 + ATK:
                    print ("You managed to knock him out. You take his stuff.\n")
                    print("CASH: +1000")
                    cash += 1000
                    print("ITEM: +KNIFE")
                    knife = True
                    return_to_game()
                    return
                else:
                    print("The loan shark stabs you, and everything goes dark.")
                    exit()
     
def start_day_tracking():
    import threading
    thread = threading.Thread(target=track_days)
    thread.daemon = True
    thread.start()

start_day_tracking()

def return_to_game():
    menu()

def menu():
    global days_passed
    
    if cash <1:
        broke()

    while True:
        os.system("cls")
        print("Welcome to the casino! | v0.2.2")
        print("by: ROLERKUPS\n")
        print("1 - Slots\n")
        print("2 - Roulette\n")

        try:
            select = input("Please select the game you'd like to play! ")
            select = int(select)
            if select == 1:
                slot()
                break
            elif select == 2:
                rouletterules()
                break
            else:
                print("Invalid Option")
                time.sleep(3)
        except ValueError:
            print("Invalid Response!")
            time.sleep(3)
            continue
        
def broke():

    global ring, cash, loan, poo, shark_tracking

    if ring == True:
        os.system("cls")
        print("You get home late from the casino, having lost all your money.")
        time.sleep(3)
        print("Without a second of hesitation you take your grandmother's engagement ring and pawn it for $450.")
        time.sleep(3)
        print("You head straight back to the casino.")
        time.sleep(3)
        ring = False
        cash = 450
        return
    elif loan == True:
        shark_tracking = days_passed
        os.system("cls")
        print("With nowhere left to turn, you set up a meet with one of the city's cruelest loan sharks.")
        time.sleep(3)
        print("The man agrees to give you $500, with the agreement you'll pay him back $1000 in five days.")
        time.sleep(3)
        print("You head straight back to the casino.")
        time.sleep(3)
        poo = True
        loan = False
        cash = 500
        return
    else:
        os.system("cls")
        print("You walk yourself home from the casino, late at night, pockets empty, and the smell of alcohol repulsing those around you.")
        time.sleep(3)
        print("You turn the corner to find the loan shark waiting for you, with a few of his goons. You won't be getting out of this one.")
        time.sleep(3)
        print("Everything goes dark.")
        time.sleep(3)
        os.system("cls")
        exit()

def gamble(bet):

    global cash
    x = max(bet // 2, 1)
    os.system("cls")
    print(f"You have ${x} to gamble.")

    while x > 0:
        
        while True:
            print("Choose your gamble:\n")
            print("1 - 50/50 gamble (win = 2x your money)")
            print("2 - 25 percent gamble (win = 4x your money)")
            print("3 - Cash out and keep your winnings!\n")

            choice = input("Enter '1', '2', or '3': ")
            if choice in ["1", "2", "3"]:
                break
            else:
                print("Invalid Choice!")
                time.sleep(3)

        if choice == "1":

            while True:
                guess = input("Pick '1' or '2': ")
                if guess in ["1", "2"]:
                    break
                else:
                    print("Invalid choice! Pick 1 or 2")
                    time.sleep(3)

            outcome = str(random.randint(1,2))
            if guess == outcome:
                x *= 2
                print(f"You won! Your gambling money is now ${x}")
                print(f"CASH: ${cash}")
                time.sleep(3)
            else:
                print("You lost your gambling money!")
                print(f"CASH: ${cash}")
                time.sleep(3)
                x = 0

        elif choice == "2":

            while True:
                guess = input("Pick a number between 1 and 4: ")
                if guess in ["1", "2", "3", "4"]:
                    break
                else:
                    print("Invalid choice! Please pick a number between 1-4")
                    time.sleep(3)

            outcome = str(random.randint(1,4))
            if guess == outcome:
                x *= 4
                print(f"You won! Your gambling money is now ${x}")
                print(f"CASH: ${cash}")
                time.sleep(3)
            else:
                print("You lost your gambling money!")
                print(f"CASH: ${cash}")
                time.sleep(3)
                x = 0

        elif choice == "3":
            cash = cash + x
            print(f"You cashed out with ${x}")
            print(f"CASH: ${cash}")
            time.sleep(3)
            break

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
    choice = input("PRESS ENTER TO CONTINUE (or type 'menu' to go back): ")
    if choice.lower() == "menu":
        return menu()
    return

def slot():
    global cash
    global slot_rules_shown

    if not slot_rules_shown:
        slotrules()
        slot_rules_shown = True  # mark rules as shown

    while True:

        if cash < 1:
            print("you broke ass mothafucka get the fuck out")
            time.sleep(3)
            broke()
            return

        while True:
            os.system("cls")
            user_input = input("ENTER YOUR BET AMOUNT (or type 'menu' to return): ")
            if user_input.lower() == "menu":
                return menu()
            try:
                bet = int(user_input)
                if bet > cash:
                    print("You don't have enough money!")
                    time.sleep(3)
                    continue
                elif bet <= 0:
                    print("Bet must be greater than 0!")
                    time.sleep(3)
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
                time.sleep(3)   
        
        cash -= int(bet)
        multiplier = 5 + (int(bet)/10)
        multiplier2 = 3 + (int(bet)/20)
        
        slot1 = random.randint(1, 9)
        slot2 = random.randint(1, 9)
        slot3 = random.randint(1, 9)
        
        print("\n",slot1,slot2,slot3,"\n")

        if slot1 == 7 and slot2 == 7 and slot3 == 7:
            winnings = int(bet) * multiplier
            print(f"You Won: ${winnings}\n")
            cash = cash + winnings
            print(f"CASH: ${cash}")
            time.sleep(3)
            continue
        elif (slot1 == 7 and slot2 == 7) or (slot1 == 7 and slot3 == 7) or (slot2 == 7 and slot3== 7):
            winnings = int(bet) * 5
            print(f"You Won: ${winnings}\n")
            cash = cash + winnings
            print(f"CASH: ${cash}")
            time.sleep(3)
            continue
        elif slot1 == 3 and slot2 == 3 and slot3 == 3:
            winnings = int(bet) * multiplier2
            print(f"You Won: ${winnings}\n")
            cash = cash + winnings
            print(f"CASH: ${cash}")
            time.sleep(3)
            continue
        elif (slot1 == 3 and slot2 == 3) or (slot1 == 3 and slot3 == 3) or (slot2 == 3 and slot3== 3):
            winnings = int(bet) * 3
            print(f"You Won: ${winnings}\n")
            cash = cash + winnings
            print(f"CASH: ${cash}")
            time.sleep(3)
            continue

        lucky_numbers = [1, 5 ,9]
        lucky_count = sum([slot1 in lucky_numbers, slot2 in lucky_numbers, slot3 in lucky_numbers])
        if lucky_count >= 2:
            print("You matched two lucky numbers! Time to gamble!")
            time.sleep(3)
            gamble(bet)
            continue

        else:
            print(f"You Lost: ${bet}\n")
            print(f"CASH: ${cash}")
            time.sleep(3)
            continue

def rouletterules():

    os.system("cls")
    print("ROULETTE RULES:\n")
    print("There are two types of bets you can make: Colours and Numbers\n")
    print("1 - Colours - Choose whether the wheel will land on black or red, win for a 2X return on your bet.")
    print("2 - Numbers - Pick a number between 1-36, if you pick the correct number you get a 35X return on your bet.\n")
    choice = input("PRESS ENTER TO CONTINUE (or type 'menu' to go back): ")
    if choice.lower() == "menu":
        return menu()
    else:
        roulette()

def roulette():

    global cash

    while True:
        if cash < 1:
            broke()
            return
        
        value = random.randint(1,2)
        value2 = random.randint(1,36)

        os.system("cls")
        print("Please select how you would like to gamble today:")
        print(f"CASH: ${cash}\n")
        print("1 - Colours")
        print("2 - Numbers\n")

        choice = input("ENTER '1' OR '2' (or type 'menu' to return): ")

        if choice.lower() == "menu":
            print("See you next time!")
            time.sleep(3)
            menu()
            return
        try:
            choice = int(choice)
            if choice not in [1, 2]:
                print("Invalid choice! Must be 1 (Colours) or 2 (Numbers).")
                time.sleep(3)
                continue
        except ValueError:
            print("Invalid input! Please enter 1 or 2.")
            time.sleep(3)
            continue

        if choice == 1:
        
            while True:
                try:
                    bet = int(input("ENTER YOUR BET AMOUNT: "))
                except ValueError:
                    print("Invalid input! Bet must be a number!")
                    time.sleep(3)
                    continue

                if bet <= 0:
                    print("Bet must be greater than 0.")
                    time.sleep(3)
                    continue
                
                if bet > cash:
                    print("You don't have enough money.")
                    time.sleep(3)
                    continue
                break

            while True:
                try:
                    y = int(input("TYPE '1' TO BET ON BLACK, TYPE '2' TO BET ON RED: "))
                    if y not in [1, 2]:
                        print("Invalid choice! Must be 1 (Black) or 2 (Red)")
                        time.sleep(3)
                        continue
                    break
                except ValueError:
                    print("Invalid input! Must be 1 or 2.")
                    time.sleep(3)

            cash -= bet
            landed = "Black" if value == 1 else "Red"
            chosen = "Black" if y == 1 else "Red"
            os.system("cls")
            print(f"It landed on {landed}!\nYou picked {chosen}!\n")

            if value == y:
                winnings = bet * 2
                cash += winnings
                print(f"You Won: ${winnings}")
                print(f"CASH: ${cash}")
            else:
                print(f"You lost: ${bet}")
                print(f"CASH: ${cash}")
            time.sleep(3)

        elif choice == 2:
            while True:
                try:
                    bet = int(input("PLACE YOUR BET AMOUNT: "))
                except ValueError:
                    print("Invalid input! Must be a number.")
                    time.sleep(3)
                    continue

                if bet <= 0:
                    print("Bet must be greater than 0!")
                    time.sleep(3)
                    continue

                if bet > cash:
                    print("You don't have enough money.")
                    time.sleep(3)
                    continue
                break
        
            while True:
                try:
                    y2 = int(input("CHOOSE A NUMBER BETWEEN 1-36 TO BET ON: "))
                    if y2 < 1 or y2 > 36:
                        print("Invalid choice! Must be between 1 and 36")
                        time.sleep(3)
                        continue
                    break
                except ValueError:
                    print("Invalid input! Must be a number between 1-36")
                    time.sleep(3)

            cash -= bet
            os.system("cls")
            print(f"It landed on {value2}!\n")
            print(f"You picked {y2}!\n")

            if value2 == y2:
                winnings = bet * 35
                cash += winnings
                print(f"You won: ${winnings}\n")
                print(f"CASH: ${cash}")
                time.sleep(3)
            else:
                print(f"You lost: ${bet}\n")
                print(f"CASH: ${cash}")
                time.sleep(3)

os.system("title CASINO")
menu()