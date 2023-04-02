"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "713138586"
secret_word: str = input("Enter a 5-character word: ")
if (len(secret_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
hidden_letter: str = input("Enter a single character: ")
if (len(hidden_letter) != 1):
    print("Error: Character must be a single character")
    exit()
print("Searching for " + hidden_letter + " in " + secret_word)
count: int = 0
if (hidden_letter == secret_word[0]):
    print(hidden_letter + " found at index 0")
    count = count + 1
if (hidden_letter == secret_word[1]):
    print(hidden_letter + " found at index 1")
    count = count + 1
if (hidden_letter == secret_word[2]):
    print(hidden_letter + " found at index 2")
    count = count + 1
if (hidden_letter == secret_word[3]):
    print(hidden_letter + " found at index 3")
    count = count + 1
if (hidden_letter == secret_word[4]):
    print(hidden_letter + " found at index 4")
    count = count + 1
if (count < 1):
    print("No instances of " + hidden_letter + " found in " + secret_word)
if (count == 1):
    print(str(count) + " instance of " + hidden_letter + " found in " + secret_word)
if (count > 1):
    print(str(count) + " instances of " + hidden_letter + " found in " + secret_word)