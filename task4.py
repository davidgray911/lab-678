#!/usr/bin/python
#wczytywanie do obiektu z pliku .yaml i weryfikacja poprawności składni pliku
import sys
import yaml
def main():
        if len(sys.argv) != 2:
                print("Dozwolony jest tylko jeden argument")
                return
        else:
                pass
open_file = sys.argv
def open_yaml(open_file):
    try:
        with open(open_file, 'r') as plik:
            a = yaml.safe_load(plik)
            return a
    except yaml.YAMLError:
        print("Taki plik nie istnieje, sprawdź nazwę")
    except FileNotFoundError:
        print("Taki plik nie istnieje")
      else:
       print("Taki plik istnieje")
