# CASINO

project game, very early release barely functional slots game is the only feature at the moment

play once you have lost all your irl money

**Commit Notes – Casino Game (v0.2.1 updates)**

- Added while True loops to ensure input prompts repeat until valid input is entered.

- Fixed all input validation bugs for:

    - Betting amounts in slots and roulette.

    - Choice selection in roulette (colours or numbers).

    - Colour selection in roulette (Black or Red).

    - Number selection in roulette (1–36).

- Corrected flow in roulette to prevent skipping steps or invalid outcomes.

- Ensured cash deduction and winnings calculation works correctly for both slots and roulette.

- Fixed recursion/return issues for menus and rules screens to prevent infinite loops or crashes.

- Cleaned up minor display and os.system("cls") issues for clearer output.

**v0.2.0**

- Added roulette feature

- Organised code

**v0.1.3**

- Expanded extra life feature (now 2 lives, with death feature)

- Fixed winnings calculation (when displaying the amount you won from a bet, it would display the wrong amount)

**v0.1.2**

- Added cash display above bet input

- Adding gambling function to slots game

**v0.1.1**

- Fixed slots game (broke when you won)

- Putting an invalid bet (not using numbers) returns you to bet input screen

- Can no longer bet more than your available currency

- Your winnings are now clearly displayed after a win

- You immediately go back to bet input screen after winning / losing a bet instead of having to press enter

- Added while true loop to slots game to prevent crashes

- Added an 'extra life' feature when you get to zero money

**v0.1**

- made menu
- made slots game
