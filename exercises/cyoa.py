"""EX06 - Choose your own adventure."""

__author__ = "713138586"

player: str = ""
points: int = 0
EMOJI_STRING: str = "\U00000000"


def main() -> None:
    """Begins the game."""
    global EMOJI_STRING
    EMOJI_STRING = "\U0001F920"
    global points
    points = 0
    global player
    playing: bool = True
    greet()
    while playing:
        adventure_decision: str = input(f"{(player)}, you will need to train up to at least 30 points total to be prepared for an attack. You currently have {(points)} points. Would you like to train? ('yes' or 'no') ")
        if adventure_decision == "no":
            playing = False
        else:
            which_way: str = input(f"Welcome to the training command post, {(player)}. Would you like to try 'archery' or 'sword fighting'? ")
            if which_way == "sword fighting":
                print(f"{(player)}, you're a brave one. Let's get outside the walls.")
                print("But first, I have a secret word that will allow you back into the gates. Unfortunately, you will have to guess it to prove your worth. You will have 6 tries to guess the password. Let's have your first guess. ")
                ground()
            else:
                if which_way == "archery":
                    print(f"{(player)}, archers are invaluable for protecting our gates. Good choice.")
                    bulls: int = input("How many years have you been shooting a bow? If you say a negative number, I'll assume you're being snarky and count it as zero. ")
                    points = tower(bulls)
    if points >= 30:
        print(f"Congratulations! You earned {(points)} points. You're ready to help protect the city! {(EMOJI_STRING)}")
    if points < 30:
        print(f"That's too bad, {(player)}! You only earned {(points)} points.You have not trained enough to help protect the city. Come back if you want to train some more! {(EMOJI_STRING)}")
                    

def greet() -> None:
    """Greeting the player."""
    print("Welcome to our city! We are in need of people to help with our defense. ")
    global player 
    player = input("What is your name? ")


def ground() -> None:
    """Begins the sword fighting adventure."""
    global player
    CODE_WORD: str = "sword"
    turn_counter: int = 1
    playing: bool = False
    while turn_counter <= 6 and playing is False:
        turn_prompt: str = f"=== Turn {(turn_counter)}/6 ==="
        print(turn_prompt)
        big_guess: str = input_guess(len(CODE_WORD))
        print(emojified(big_guess, CODE_WORD))
        if big_guess == CODE_WORD:
            print(f"You won in {(turn_counter)}/6 turns!")
            global points
            points += 5
            playing = True
        else:
            turn_counter = turn_counter + 1
    if playing is False:
        print("X/6 - Sorry, try again tomorrow!")
        
        
def tower(bullseye: int) -> int:
    """Begins the archery adventure."""
    global points
    from random import randint
    score: int = points
    global player
    playing: bool = True
    while playing:
        test: str = input(f"Go ahead and take a practice shot at the target to see your score, {(player)}. (type 'shoot' or 'don't shoot') ")
        if test == "shoot":
            if score < 30:
                shooting_score: int = randint(0, 3)
                score += 3
                print(f"Great practice! You shot a {(shooting_score)}. We will only count each practice shot as one point toward your training, {(player)}. You now have a total of {(score)} points! Keep going to reach 30 or type 'don't shoot' to return to the main menu. ")
            else:
                if score >= 10:
                    score += 5
                    print(f"Bullseye! You're well trained. You now have {(score)} points. Feel free to keep practicing or try another training exercise.")
        else:
            if test == "don't shoot":
                print("No worries. Come back and try again sometime if you would like!")
                playing = False
    return score
        

def contains_char(word_guess: str, letter: str) -> bool:
    """Searches the guessed word for the letter."""
    assert len(letter) == 1
    word_idx: int = 0
    while word_idx < len(word_guess):
        if word_guess[word_idx] == letter:
            return True
        else:
            word_idx += 1
    else:
        return False


def emojified(secret_guess: str, secret_word: str) -> str:
    """Creates colored boxes for feedback on guess."""
    assert len(secret_guess) == len(secret_word)
    secret_idx: int = 0
    guess_box: str = ""
    while secret_idx < len(secret_word):
        if secret_guess[secret_idx] == secret_word[secret_idx]:
            guess_box += "\U0001F7E9"
        else:
            if (contains_char(secret_word, secret_guess[secret_idx])) is True:
                guess_box += "\U0001F7E8"
            else:
                guess_box += "\U00002B1C"
        secret_idx += 1
    return guess_box


def input_guess(expected_length: int) -> str:
    """Determines if guess is the same length as secret word."""
    guess: str = input(f"Enter a {(expected_length)} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {(expected_length)} chars! Try again: ")
    return guess


if __name__ == "__main__":
    main()