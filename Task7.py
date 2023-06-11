#!/usr/bin/python
#zapis danych z obiektu do pliku w formacie i zgodnie ze składnią .xml
import sys
import xmltodict
def main():
        if len(sys.argv) != 2:
                print("Dozwolony jest tylko jeden argument")
                return
        else:
                pass
save_file = sys.argv
a = None
def save_xml(a, save_file):
    try:
        with open(a, 'w') as plik:
            xml_str = xmltodict.unparse(save_file, pretty=True)
            plik.write(xml_str)
        print("Udana konwersja do formatu XML")
    except Exception:
        print("Błąd")

