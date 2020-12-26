This project is a "mastermind brute force assistant".
Given a list of codes, the number of colors in correct slots, and number of colors in wrong slots, this script returns a list of possible secret codes.
This helps the guesser quickly arrive at the secret code.

There are algorithms that can always win the game in 5 guesses or less (https://en.wikipedia.org/wiki/Mastermind_%28board_game%29), but I've found I can usually win in 5 or less guesses just by randomly selecting a possible secret code.

Mastermind is available to play at (https://www.archimedes-lab.org/mastermind.html).

I was at Target and saw a copy of Mastermind and thought I could code something up to automate some of the drudgery of figuring possible guesses, and that this would be a good opportunity to learn some basics of pytest, mypy, and typing.
I was inspired by Joel Grus's live coding session on neural nets.
