# Mastermind brute force assistant

Mastermind is a two player game where one player (the codemaker) makes a secret code, and the other player (the guesser) has 10 attempts to guess the secret code.
This project is a "mastermind brute force assistant".
Given a list of attempted codes, the number of colors in correct slots, and number of colors in wrong slots, this script returns a list of possible secret codes.
This helps the guesser quickly arrive at the secret code.
Mastermind is available to play at https://www.archimedes-lab.org/mastermind.html.

To use:
1. run `assistant.py` interactively (`ipython -i assistant.py`).
2. Make guesses and append your guesses to `attempts`.
For example, append `Code("RBGO", black=2, white=1)` to `attempts`.
The capital letters correspond to the 6 colors (blue, green, orange, purple, red, yellow).
3. To get the list of possible codes, run `list(all_possible_codes(all_codes, attempts))`.
4. Repeat.

There are algorithms that can always win the game in 5 guesses or less (https://en.wikipedia.org/wiki/Mastermind_%28board_game%29), but I've found I can usually win in 6 or less guesses just by randomly selecting a possible secret code.

I was at Target and saw a copy of Mastermind and thought I could code something up to automate some of the drudgery of figuring possible guesses, and that this would be a good opportunity to learn some basics of object oriented programming, pytest, and mypy.
I was inspired by Joel Grus's live coding session on neural nets.
