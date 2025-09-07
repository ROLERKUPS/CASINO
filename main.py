# LAST UPDATED 7/09/2025 9:58 PM

import random
import os
import time
import threading

def get_choice(prompt, valid_choices):
    while True:
        choice = input(prompt)
        if choice.lower() == "menu":
            return "menu"
        try:
            choice = int(choice)
            if choice in valid_choices:
                return choice
            else:
                print(f"Invalid choice! Pick {valid_choices}")
        except ValueError:
            print("Invalid input! Must be a number.")

class Player:
    def __init__ (self, name, cash=500):
        self.name = name
        self.cash = cash
        self.ring = True
        self.knife = False
        self.loan = True
        self.poisoned = False
        self.ATK = 0

    def add_cash(self, amount):
        self.cash += amount
        print(f"You gained ${amount}. Current cash: ${self.cash}")

    def lose_cash(self, amount):
        self.cash -= amount
        print(f"You lost ${amount}. Current cash: ${self.cash}")

    def pawn_ring(self):
        if self.ring:
            self.ring = False
            self.cash += 450
            print(f"You pawned the ring for $450. Current cash: ${self.cash}")

    def take_loan(self, loan_shark, day_tracker):
        if self.loan:
            self.cash += 500
            self.loan = False
            self.poisoned = True
            loan_shark.tracking_day = day_tracker.day
            print(f"You took a loan for $500. Cash: ${self.cash}")
        else:
            print("You need to sort out your debt first.")

    def fight_loan_shark(self):
        fight_chance = random.randint(1,100)
        if fight_chance <= 10 + self.ATK:
            print("You knocked out the loan shark and took $1000 and a knife!")
            self.cash += 1000
            self.knife = True
        else:
            print("You were stabbed to death by the loan shark. Game Over!")
            time.sleep(3)
            exit()

    def negotiate_loan_shark(self):
        chance = random.randint(1,100)
        if chance <= 50:
            print("You were beaten badly, and now must pay the loan shark $2000 by tomorrow.")
        else:
            print("The loan shark stabbed you to death in a fit of rage. Game Over!")
            time.sleep(3)
            exit()

class LoanShark:
    def __init__(self, player):
        self.player = player
        self.tracking_day = 0
    
    def confront(self):
        print("The loan shark drags you into a nearby alley, knife in hand!")
        time.sleep(2)
        print("He furiously demands the payment of $1000 you owe him.")
        time.sleep(2)

        if self.player.cash >= 1000:
            print("1. Pay $1000\n2. Refuse to pay (fight)\n3. Try to negotiate")
            choice = get_choice("Select 1, 2, or 3: ", [1, 2, 3])
            if choice == "menu":
                return
            if choice == 1:
                self.player.lose_cash(1000)
                print("You pay the loan shark, and he leaves in a hurry.")
            elif choice == 2:
                self.player.fight_loan_shark()
            elif choice == 3:
                 self.player.negotiate_loan_shark()
        else:
            print("You don't have enough money to pay him back.")
            print("1. Attempt to negotiate\n2. Refuse to pay (fight)\n")
            choice = get_choice("Select 1 or 2 ", [1, 2])
            if choice == "menu":
                return
            if choice == 1:
                self.player.negotiate_loan_shark()
            elif choice == 2:
                self.player.fight_loan_shark()

class GameDayTracker:
    def __init__(self, player, loan_shark):
        self.player = player
        self.loan_shark = loan_shark
        self.day = 0

    def next_day(self):
        self.day += 1
        print(f"DAY: {self.day}")
        if self.player.poisoned and self.day >= self.loan_shark.tracking_day + 5:
            self.loan_shark.confront()
            self.loan_shark.tracking_day = self.day

class CasinoGame:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.loan_shark = LoanShark(self.player)
        self.day_tracker = GameDayTracker(self.player, self.loan_shark)
        self.slot_rules_shown = False

    def start(self):
        threading.Thread(target=self.track_days, daemon = True).start()
        self.menu()

    def track_days(self):
        while True:
            time.sleep(150)
            self.day_tracker.next_day()

    def menu(self):
        while True:
            os.system("cls")
            print(f"Welcome to the Casino, {self.player.name}! | v0.2.2")
            print("by: ROLERKUPS\n")
            print("1. Slots\n2. Roulette\n")
            choice = int(input("Select either 1 or 2 to play a game: "))
            if choice == 1:
                self.slot()
            elif choice == 2:
                self.roulette()
            else:
                print("Invalid Choice!")
                time.sleep(2)

    def slot(self):
        if not self.slot_rules_shown:
            self.slotrules()
            self.slot_rules_shown = True

        while True:

            if self.player.cash < 1:
                print("you broke ass mothafucka get the fuck out")
                time.sleep(3)
                self.broke()
                return

            while True:
                os.system("cls")
                user_input = input("ENTER YOUR BET AMOUNT (or type 'menu' to return): ")
                if user_input.lower() == "menu":
                    return
                try:
                    bet = int(user_input)
                    if bet > self.player.cash:
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
            
            self.player.cash -= int(bet)
            multiplier = 5 + (int(bet)/10)
            multiplier2 = 3 + (int(bet)/20)
            
            slot1 = random.randint(1, 9)
            slot2 = random.randint(1, 9)
            slot3 = random.randint(1, 9)
            
            print("\n",slot1,slot2,slot3,"\n")

            if slot1 == 7 and slot2 == 7 and slot3 == 7:
                winnings = int(bet) * multiplier
                print(f"You Won: ${winnings}\n")
                self.player.cash += winnings
                print(f"CASH: ${self.player.cash}")
                time.sleep(3)
                continue
            elif (slot1 == 7 and slot2 == 7) or (slot1 == 7 and slot3 == 7) or (slot2 == 7 and slot3== 7):
                winnings = int(bet) * 5
                print(f"You Won: ${winnings}\n")
                self.player.cash += winnings
                print(f"CASH: ${self.player.cash}")
                time.sleep(3)
                continue
            elif slot1 == 3 and slot2 == 3 and slot3 == 3:
                winnings = int(bet) * multiplier2
                print(f"You Won: ${winnings}\n")
                self.player.cash += winnings
                print(f"CASH: ${self.player.cash}")
                time.sleep(3)
                continue
            elif (slot1 == 3 and slot2 == 3) or (slot1 == 3 and slot3 == 3) or (slot2 == 3 and slot3== 3):
                winnings = int(bet) * 3
                print(f"You Won: ${winnings}\n")
                self.player.cash += winnings
                print(f"CASH: ${self.player.cash}")
                time.sleep(3)
                continue

            lucky_numbers = [1, 5 ,9]
            lucky_count = sum([slot1 in lucky_numbers, slot2 in lucky_numbers, slot3 in lucky_numbers])
            if lucky_count >= 2:
                print("You matched two lucky numbers! Time to gamble!")
                time.sleep(3)
                self.gamble(bet)
                continue

            else:
                print(f"You Lost: ${bet}\n")
                print(f"CASH: ${self.player.cash}")
                time.sleep(3)
                continue

    def roulette(self):

        while True:
            if self.player.cash <1:
                self.broke()
                return
            
            value = random.randint(1,2)
            value2 = random.randint(1,36)

            os.system("cls")
            print("Please select how you would like to gamble today:")
            print(f"CASH: ${self.player.cash}\n")
            print("1 - Colours")
            print("2 - Numbers\n")

            choice = input("ENTER '1' OR '2' (or type 'menu' to return): ")

            if choice.lower() == "menu":
                print("See you next time!")
                time.sleep(3)
                self.menu()
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
                    
                    if bet > self.player.cash:
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

                self.player.cash -= bet
                landed = "Black" if value == 1 else "Red"
                chosen = "Black" if y == 1 else "Red"
                os.system("cls")
                print(f"It landed on {landed}!\nYou picked {chosen}!\n")

                if value == y:
                    winnings = bet * 2
                    self.player.cash += winnings
                    print(f"You Won: ${winnings}")
                    print(f"CASH: ${self.player.cash}")
                else:
                    print(f"You lost: ${bet}")
                    print(f"CASH: ${self.player.cash}")
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

                    if bet > self.player.cash:
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

                self.player.cash -= bet
                os.system("cls")
                print(f"It landed on {value2}!\n")
                print(f"You picked {y2}!\n")

                if value2 == y2:
                    winnings = bet * 35
                    self.player.cash += winnings
                    print(f"You won: ${winnings}\n")
                    print(f"CASH: ${self.player.cash}")
                    time.sleep(3)
                else:
                    print(f"You lost: ${bet}\n")
                    print(f"CASH: ${self.player.cash}")
                    time.sleep(3)

    def slotrules(self):
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
            return
        return

    def broke(self):
        if self.player.ring == True:
            os.system("cls")
            print("You get home late from the casino, having lost all your money.")
            time.sleep(3)
            print("Without a second of hesitation you take your grandmother's engagement ring and pawn it for $450.")
            time.sleep(3)
            print("You head straight back to the casino.")
            time.sleep(3)
            self.player.ring = False
            self.player.cash = 450
            return
        elif self.player.loan:
            self.loan_shark.tracking_day = self.day_tracker.day
            os.system("cls")
            print("With nowhere left to turn, you set up a meet with one of the city's cruelest loan sharks.")
            time.sleep(3)
            print("The man agrees to give you $500, with the agreement you'll pay him back $1000 in five days.")
            time.sleep(3)
            print("You head straight back to the casino.")
            time.sleep(3)
            self.player.poisoned = True
            self.player.loan = False
            self.player.cash = 500
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

    def gamble(self, bet):
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
                    print(f"CASH: ${self.player.cash}")
                    time.sleep(3)
                else:
                    print("You lost your gambling money!")
                    print(f"CASH: ${self.player.cash}")
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
                    print(f"CASH: ${self.player.cash}")
                    time.sleep(3)
                else:
                    print("You lost your gambling money!")
                    print(f"CASH: ${self.player.cash}")
                    time.sleep(3)
                    x = 0

            elif choice == "3":
                self.player.cash += x
                print(f"You cashed out with ${x}")
                print(f"CASH: ${self.player.cash}")
                time.sleep(3)
                break

os.system("title CASINO")
game = CasinoGame("Jeff")
game.start()