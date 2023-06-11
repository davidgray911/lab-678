#!/usr/bin/python
#wczytywanie do obiektu z pliku .xml i weryfikacja poprawności składni pliku
import sys
import xmltodict
def main():
        if len(sys.argv) != 2:
                print("Dozwolony jest tylko jeden argument")
                return
        else:
                pass
open_file = sys.argv
a = None
def open_xml(open_file):
    try:
        with open(open_file, 'r') as plik:
            a = xmltodict.parse(plik.read())
            return a
    except FileNotFoundError:
        print("Taki plik nie istnieje")
    else:
        print("Taki plik istnieje")

