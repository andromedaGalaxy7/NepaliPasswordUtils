import os
import bisect

class EnglishDictionary:

    def __init__(self, wordlist_file:str, min_length:int=1, sorted_wordlist:bool=False, force_lowercase:bool=True):
        """Create an EnglishDictionary object

        Args:
            wordlist_file (str): The file containing valid words
            min_length (int, optional): Minimum number of letters needed in the word to be accepted
            sorted_wordlist (bool, optional): True if the words are sorted already in the file.
            force_lowercase (bool, optional): Convert all the words to lowercase for uniformity and ease. 
        """
        self.wordlist_file = wordlist_file
        self.min_length = min_length
        self.sorted_wordlist = sorted_wordlist
        self.force_lowercase = force_lowercase
        self.words = []
        self.words_length = 0

    
    def load_words(self):
        """
        Load words from the provided wordlist file into the `words` array  
        """
        with open(self.wordlist_file) as f:
            word = f.readline()
            while word:
                word = word.strip("\r\n ")
                if self.force_lowercase:
                    word = word.lower()
                if len(word) > self.min_length:
                    self.words.append(word)
        
        # Sort the words
        if not self.sorted_wordlist:
            self.words.sort()

        # Update the length
        self.words_length = len(self.words)

    def is_valid_word(self, word):
        """Check if a word is in the dictionary

        Args:
            word (str): Word to look up
        """
        if bisect.bisect_left(word) < self.words_length:
            return True
        return False
