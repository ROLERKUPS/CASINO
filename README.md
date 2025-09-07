# CASINO

project game, very early release barely functional slots game is the only feature at the moment

play once you have lost all your irl money

**Commit Notes - Casino Game (v0.2.3 updates)**

get_choice function (input validation function)

- ensures that inputs requiring integer responses are valid, numeric, or allow "menu" to return.
- cleans up code, allowing for removal of some while true loops and try/except blocks (hasn't been implemented through entire code as i am lazy and cbf rn)

- removed core game functions and turned them into classes (Player, Loanshark, GameDayTracker, CasinoGame)

- reduced size of code a lot, made it easier to store and access information.
- loan shark logic is in its own class, interacts cleanly with Player
- day tracking is in its own GameDayTracker
- casino games and stuff are in CasinoGame
- overall this just makes understanding, maintaining and scaling the code a lot easier now

**Commit Notes - Casino Game (v0.2.2 updates)**

- Day Tracking System Added
The game now tracks days (each day is 180 seconds), and after three minutes a new day passes.

- Loan Shark Event Added
Due to the game now being able to track days, when the loan shark gives you the loan after 5 days it triggers an event where you actually have to pay the loan or find another way to deal with it.

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
