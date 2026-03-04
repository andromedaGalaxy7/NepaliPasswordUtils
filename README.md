# Nepali Password Utilities
This repo contains a set of password utilities, particularly handy for those who are testing and trying to crack WPA2 handshakes.

A lot of passwords in Nepal usually have the format:
`name_of_a_person_or_place` + `some_symbol` + `some_number`

The repo contains a set of data extractors that can extract Nepali common names and some Hindi names(since we share a lot of names with hindi too) from a few popular websites.

It contains two directories

### 1. `data_extractors/`
Contains a set of python scripts to extract names from common "Nepali names and their meanings" kind of websites.

And also contains a set of pre-generated list of Nepali and hindi girl and boys names,
and a list of nepali districts and municipalities name.

### 2. `password_utilities/`

 Contains two sub directories to two python programs:

#### i. `password_munger`
Contains a script `word_munger.py` that can generate commonly generated passwords from one word.

Usage:
```C
python3 word_munger.py somename
```
And it generates a file output.txt with:
```
somename
SOMENAME
Somename
sOmename
soMename
somEname
someName
somenAme
somenaMe
somenamE
sOMENAME
SoMENAME
SOmENAME
SOMeNAME
SOMEnAME
SOMENaME
SOMENAmE
SOMENAMe
somename!
..... And millions more. You get the idea !!! 
```

The other file `munger_utils.py` just contains the functions that the main program uses !!!
#### ii. `wordlists_merger`

The data extractors written to extract nepali names do not save them all into one single wordlist. Therefore, the `wordlists_merger` is there so that it can collect all the `*.txt` files from the `data_extractors` directory and save them into a single `masterwordlist.txt` file.

Usage:
```C
python3 wordlist_merger.py
```
 If you wish to change the location of where you scattered wordlists are, just edit the file `wordlist_merger.py`

 and change line 13:
 
```python
DIRECTORIES_LIST = ["../../data_extractors"]
```

## 🎉🎉 HAPPY PASSWORD CRACKING FOLKS 🎉🎉
