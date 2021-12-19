import requests
from urllib.parse import quote
from os import system
replurl = "YOUR REPL WEBSIDE URL"

def cls():
    try:
        system("cls")
    except:
        system("clear")
cls()     
   
while True:
    command = input("command> ")
    if command == "cls":
        cls()
    else:
        a = quote(command.encode('utf-8'))
        r = requests.get(f"{replurl}/cmd/{a}")
        print(r.text)