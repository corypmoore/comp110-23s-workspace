"""One shot wordle exercise."""

__author__ = "713138586"

SECRET_WORD: str = "python"
guess: str = input(f"What is your {len(SECRET_WORD)}-letter guess? ")
playing: bool = True
guess_idx: int = 0
input_idx: int = 0
alt_idx: int = 0
guess_box: str = ""
close_guess: bool = False

while playing:
    """Checking to see if user guess matches the secret word"""
    if (guess == SECRET_WORD):
        while input_idx < len(SECRET_WORD):
            if guess[input_idx] == SECRET_WORD[input_idx]:
                guess_box = guess_box + "\U0001F7E9"
            else:
                guess_box = guess_box + "\U00002B1C"
            input_idx = input_idx + 1
        print(guess_box)
        print("Woo! You got it!")
        playing = False
    else:
        if (len(guess) != len(SECRET_WORD)):
            """Checking to see if the length of the guess is the same length as the secret word"""
            guess = input(f"That was not {len(SECRET_WORD)} letters! Try again: ")
            guess_idx = guess_idx + 1
            if guess_idx == 6:
                print("Not quite. Play again soon!")
                playing = False
        else:
            """If guess is correct length but not the correct word, checking to see what letters match"""
            if (guess != SECRET_WORD):
                while input_idx < len(SECRET_WORD):
                    """If letter of the guess word matches the secret word, will add a green box"""
                    if guess[input_idx] == SECRET_WORD[input_idx]:
                        guess_box = guess_box + "\U0001F7E9"
                    else:
                        """Checking to see if letter in the guess word is found anywhere else in the secret word"""
                        while close_guess is False and (alt_idx < len(SECRET_WORD)):
                            if guess[input_idx] == SECRET_WORD[alt_idx]:
                                guess_box = guess_box + "\U0001F7E8"
                                close_guess = True
                            else:
                                alt_idx = alt_idx + 1
                        else:
                            if close_guess is False:
                                guess_box = guess_box + "\U00002B1C"
                            alt_idx = 0
                        close_guess = False
                    input_idx = input_idx + 1
                print(guess_box)
                print("Not quite. Play again soon!")
                playing = False