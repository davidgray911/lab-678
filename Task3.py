#!/usr/bin/python
#zapis danych z obiektu do pliku w formacie i zgodnie ze składnią .json
import sys
import json
def main():
        if len(sys.argv) != 2:
                print("Dozwolony jest tylko jeden argument")
                return
        else:
                pass
save_file = sys.argv
a = None
def save_json(a, save_file):
    try:
        with open(save_file, 'w') as plik:
            json.dump(a, plik)
        print("Udana konwersja do formatu JSON")
    except Exception:
        print("Błąd")

