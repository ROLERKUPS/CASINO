# CASINO

project game, very early release barely functional slots game is the only feature at the moment

play once you have lost all your irl money

**Commit Notes - Casino Game (v0.2.2 updates)**

- Loan Shark Event Added
When the player runs out of money and has already pawned their grandmother's ring, they are forced to take a loan from one of the city's most dangerous loan sharks
        - Loan details: The player receives $500, but must pay back $1000 in 5 days.
        - Failure to pay the loan back on time will result in severe consequences, escalating the danger as the story 
          progresses.

- Tracking Days System Implemented
A new **day tracking** system has been added to create a sense of urgency and time pressure.
        - Each day spent gambling is now tracked (each day is 180 seconds), and as the player gets closer to the 5-day 
          deadline to repay the loan, the pressure increases.
        - This system ensures a more immersive, high-stakes experience as players race against time to recover their money.

- Increased Stakes & Desperation
The loan shark system, along with the day tracking feature, raises the stakes and adds layers of urgency, forcing the player to carefully manage their time and decisions to avoid falling deeper into trouble.

**Commit Notes - Casino Game (v0.2.1a updates)**

Fixed

- Slot rules no longer repeatedly display during spins; shown only once per session entry.

- Menu navigation no longer re-triggers slot or roulette rules unnecessarily.

- Corrected slot random number generation and multiplier calculations for accurate outcomes.

Changed / Improved

- Added input validation across all user prompts to prevent crashes from invalid entries.

- String-based inputs are case-insensitive using .lower() where applicable.

- Optimized screen clearing (cls) to prevent overlapping commands; clears only when necessary.

- Standardized time.sleep() durations for consistent pacing throughout the game.

- Cash amount now displays consistently throughout the game for better clarity.

Notes

- Core gameplay mechanics remain unchanged; updates focus on bug fixes, input handling, and UI clarity.

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
