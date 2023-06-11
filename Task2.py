#!/usr/bin/python
#wczytywanie do obiektu z pliku .json i weryfikacja poprawności składni pliku
import sys
import json
def main():
        if len(sys.argv) != 2:
                print("Dozwolony jest tylko jeden argument")
                return
        else:
                pass
open_file = sys.argv
a = None
def open_json(open_file):
    try:
        with open(open_file, 'r') as plik:
            a = json.load(plik)
            return a
    except json.JSONDecodeError:
        print("Taki plik nie istnieje, sprawdź nazwę")
    except FileNotFoundError:
        print("Taki plik nie istnieje")
    else:
        print("Taki plik istnieje")

