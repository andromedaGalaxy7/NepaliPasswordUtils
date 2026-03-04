"""
Tools and functions that work on passwords
and modify them
"""

symbols_to_append = "!@#$%^&*()-+"
wordlist = []

def upper():
    for _ in range(len(wordlist)):
        word  = wordlist[_]
        new_word = word.upper()
        wordlist.append(new_word)

def capitalize():
    for _ in range(len(wordlist)):
        word  = wordlist[_]
        if word.upper() == word:
            for i in range(len(word)):
                new_word = word[:i] + word[i].lower() + word[i+1:]
                wordlist.append(new_word)
        else:
            for i in range(len(word)):
                new_word = word[:i] + word[i].upper() + word[i+1:]
                wordlist.append(new_word)

def append_symbols():
    for _ in range(len(wordlist)):
        word  = wordlist[_]
        for symbol in symbols_to_append:
            new_word = word + symbol
            wordlist.append(new_word)

def append_numbers(max_number=10_000):
    numbers_buffer = set()
    number_of_digits = len(str(max_number))    
    for _ in range(len(wordlist)):
        word  = wordlist[_]
        for i in range(max_number+1):
            for n in range(number_of_digits):
                new_word = word + str(i).rjust(n, "0")
                numbers_buffer.add(new_word)
    
    for num in numbers_buffer:
        wordlist.append(num)