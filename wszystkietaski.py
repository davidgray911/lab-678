#!/usr/bin/python
import sys
import json
import yaml
import xmltodict


#Task2
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


#Task3
def save_json(a, save_file):
    try:
        with open(save_file, 'w') as plik:
            json.dump(a, plik)
        print("Udana konwersja do formatu JSON")
    except Exception:
        print("Błąd")


#Task4
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


#Task5
def save_yaml(a, save_file):
    try:
        with open(save_file, 'w') as plik:
            yaml.dump(a, plik)
        print("Udana konwersja do formatu YML")
    except Exception:
        print("Błąd")


#Task6
def open_xml(open_file):
    try:
        with open(open_file, 'r') as plik:
            a = xmltodict.parse(plik.read())
            return a
    except FileNotFoundError:
        print("Taki plik nie istnieje")
    else:
        print("Taki plik istnieje")


#Task7
def save_xml(a, save_file):
    try:
        with open(a, 'w') as plik:
            xml_str = xmltodict.unparse(save_file, pretty=True)
            plik.write(xml_str)
        print("Udana konwersja do formatu XML")
    except Exception:
        print("Błąd")


#Task1
def main():
    if len(sys.argv) != 3:
        print("Dozwolone sa tylko dwa argumenty")
        return
    else:
        pass

    open_file = sys.argv[1]
    save_file = sys.argv[2]

    a = None

    if open_file.endswith('.json'):
        a = open_json(open_file)
    elif open_file.endswith('.yaml'):
        a = open_yaml(open_file)
    elif open_file.endswith('.xml'):
        a = open_xml(open_file)
    else:
        print("Błędny format pliku.")
        return

    if save_file.endswith('.json'):
        save_json(a, save_file)
    elif save_file.endswith('.yaml'):
        save_yaml(a, save_filej)
    elif save_file.endswith('.xml'):
        save_xml(a, save_file)
    else:
        print("Błędny format pliku.")
        return


# ~~~~~~~~~~~ Start programu ~~~~~~~~~~~
if __name__ == '__main__':
    main()
