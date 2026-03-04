import requests
import os
import re

# SCRAPER PARAMETERS
FORMATTER_STRING = "https://www.easynepalityping.com/resource_dynamic/babynames/nepal/nepal{GENDER}{LETTER}.html"
OUTPUT_FOLDER = "easynepalityping.com"
VERBOSE = True
PATTERN = r"<td\srel=.+?>(.+?)<td"

def create_folder(path):
    """Create a folder if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def extract_names():
    create_folder(OUTPUT_FOLDER)
    for gender in ("Boy", "Girl"):
        for i in range(26):
            letter = chr(65 + i) # 65 is A
            url_to_load = FORMATTER_STRING.format(LETTER=letter, GENDER=gender)
            name_of_file_to_write = f"{gender}_{letter}.txt"
            
            file_to_write = open(OUTPUT_FOLDER + "/" + name_of_file_to_write, "w") 
            

            if VERBOSE:
                print(f"Fetching:: {url_to_load}")

            response = requests.get(url_to_load)

            matching_groups = re.findall(PATTERN, response.text)
            if VERBOSE:
                print(f"Extracting names for {gender} starting with {letter}...")

            for group in matching_groups:
                group = group.strip("\n").strip(" ")
                if VERBOSE:
                    print(f"\t{group}")
                file_to_write.write(group + "\n")
            file_to_write.close()

if __name__ == "__main__":
    extract_names()