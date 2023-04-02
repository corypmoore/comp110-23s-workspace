

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

def mimic_letter(my_words: str, letter_idx: int) -> str:
    if letter_idx > len(my_words):
        print("Too high of an index")
    else:
        return my_words[letter_idx]

my_words: str = "hi"
letter_idx: int = len(my_words)

mimic("hello there")
print(mimic("hello there"))

mimic_letter("hello",0)
print(mimic_letter("hello", 0))





