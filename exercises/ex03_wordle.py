"""Structured wordle exercise."""

__author__ = "713138586"

def contains_char(word_guess: str, letter: str) -> bool:
    """Searches the guessed word for the letter"""
    assert len(letter) == 1
    word_idx: int = 0
    while word_idx < len(word_guess):
        if word_guess[word_idx] == letter:
            return True
        else:
            word_idx = word_idx + 1
    else:
        return False

def emojified(secret_guess: str, secret_word: str) -> str:
    """Creates colored boxes for feedback on guess"""
    assert len(secret_guess) == len(secret_word)
    secret_idx: int = 0
    guess_box: str = ""
    guessing_bool: bool = False
    while secret_idx < len(secret_word):
        if secret_guess[secret_idx] == secret_word[secret_idx]:
            guess_box = guess_box + "\U0001F7E9"
        else:
            if (contains_char(secret_word, secret_guess[secret_idx])) == True:
                guess_box = guess_box + "\U0001F7E8"
            else:
                guess_box = guess_box + "\U00002B1C"
        secret_idx = secret_idx + 1
    return guess_box

def input_guess(expected_length: int) -> str:
    guess: str = input(f"Enter a {(expected_length)} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {(expected_length)} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    CODE_WORD: str = "codes"
    turn_counter: int = 1
    playing: bool = False
    while turn_counter <= 6 and playing is False:
        turn_prompt: str = f"=== Turn {(turn_counter)}/6 ==="
        print(turn_prompt)
        big_guess: str = input_guess(len(CODE_WORD))
        print(emojified(big_guess, CODE_WORD))
        if big_guess == CODE_WORD:
            print(f"You won in {(turn_counter)}/6 turns!")
            playing = True
        else:
            turn_counter = turn_counter + 1
    if playing is False:
        print("X/6 - Sorry, try again tomorrow!")
    
if __name__ == "__main__":
    main()