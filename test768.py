name: Testowanie
aplikacji
z
installResources.sh
on:
push:
branches:
- master
schedule:
- cron: '0 15 * * 3'  # odpala się co środę o 15
workflow_dispatch:

jobs:
build:

runs - on: windows - latest  # utsawienie domyslnego serwera na windows

steps:
- name: Sprawdzenie
repozytoriumm
uses: actions / checkout @ v3

- name: Setup
Pythona
uses: actions / setup - python @ v3
with:
    python - version: "3.10"

- name: Instalacja
wymaganych
bibliotek
run: bash
installResources.sh

- name: Odpalenie
skryptu
run: python
wszystkietaski.py

- name: Przesyłanie
utworzonego
pliku
uses: actions / upload - artifact @ v3
with:
    name: newpyinstaller.exe
    path: ${{github.workspace}} / newpyinstaller.exe