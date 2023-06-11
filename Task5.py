#!/usr/bin/python
#zapis danych z obiektu do pliku w formacie i zgodnie ze składnią .yaml
import sys
import yaml
def main():
        if len(sys.argv) != 2:
                print("Dozwolony jest tylko jeden argument")
                return
        else:
                pass
save_file = sys.argv
a = None
def save_yaml(a, save_file):
    try:
        with open(save_file, 'w') as plik:
            yaml.dump(a, plik)
        print("Udana konwersja do formatu YAML")
    except Exception:
        print("Błąd")

