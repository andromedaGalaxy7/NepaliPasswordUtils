"""
Combines data collected from different sources
and pre formatted
and creates a combined Nepali wordlist
"""

import os
from endict import EnglishDictionary
from utils import *

# Parameters for the create_single_wordlist function
FILE_LIST = []
DIRECTORIES_LIST = ["../../data_extractors"]
ENGLISH_DICTIONARY_FILE = "data/words_alpha.txt"
OUTPUT_FILENAME = "masterwordlist.txt"
WHITESPACE_EQUIVALENT = "@/."
MIN_LENGTH = 3

# Describes to deal with double words in a single line
IGNORE = 0
REJECT = 1
SPLIT = 2
SPLIT_BUT_KEEP_BOTH = 3
DOUBLE_WORDS = SPLIT

# Object parameters
dictionary = EnglishDictionary(ENGLISH_DICTIONARY_FILE)

def error(error_message):
    """Shows error

    Args:
        error_message (str): The error message to show on the screen
    """
    print("\tERROR: ", error_message)

def create_single_wordlist(ignore_english_words=True):
    """
    Creates one ultimate wordlist
    Args:
        ignore_english_words (bool, optional): Remove english words from the final wordlist. Defaults to True.
    """
    # Parse the directories first
    for directory in DIRECTORIES_LIST:
        list_of_files = os.listdir(directory)
        try:
            for dirpath, _, filenames in os.walk(directory):
                for file in filenames:
                    if file.lower().endswith(".txt"):
                        full_path = os.path.join(dirpath, file)
                        FILE_LIST.append(full_path)
                    
        except FileNotFoundError as e:
            error(f"Can't list the files from {directory}. No such path.")
    
    # Read and combine everything to one file
    with open(OUTPUT_FILENAME, "w") as out:
        for input_file in FILE_LIST:
            with open(input_file) as in_:
                line = in_.readline()
                
                while line:
                    line = line.strip("\r\n ").lower()
                    for char in WHITESPACE_EQUIVALENT:
                        line = line.replace(char, " ")

                    # Handle double words in one line
                    if DOUBLE_WORDS == IGNORE:
                        words = [line]
                    else:
                        if line.find(" ") > 0:
                            if DOUBLE_WORDS == REJECT:
                                words = []
                        else:
                            words = line.split(" ") # SPLIT
                            if DOUBLE_WORDS == SPLIT_BUT_KEEP_BOTH:
                                words.append(line)

                    # Process all words in the list
                    for word in words:
                        word = word.replace(" ", "")
                        if ignore_english_words:
                            if EnglishDictionary.is_valid_word(word):
                                continue
                        if len(word) >= MIN_LENGTH:
                            out.write(word + "\n")
                    line = in_.readline()
    
if __name__ == "__main__":
    create_single_wordlist(ignore_english_words=False)
