"""
Modifies a word and creates
a munged wordlist out of it
"""

import sys
from munger_utils import *
import os

order_of_operation = [upper, capitalize, append_symbols, append_numbers, append_symbols]
output_file = "output.txt"
help_docstring = """
    Usage: python word_munger.py word_to_munge output_file_name
    OR:
    python word_munger.py input_file_with_words output_file_name
"""

def start_munging():
    for func in order_of_operation:
        func()
    
    with open(output_file, "w") as f:
        for word in wordlist:
            f.write(word + "\n")

def parse_args():
    if len(sys.argv) >= 2:
        # Check if its a path
        if os.path.exists(sys.argv[1]) and os.path.isfile(sys.argv[1]):
            with open(sys.argv[1]) as f:
                line = f.readline()
                while line:
                    line = line.strip("\r\n")
                    if line:
                        wordlist.append(line)
                    line = f.readline()

        else:
            wordlist.append(sys.argv[1])

        # Change output
        if len(sys.argv) >= 3:
            globals()["output_file"] = sys.argv[2]
    else:
        print(help_docstring)

if __name__ == "__main__":
    parse_args()
    start_munging()