import logging
from art import *

def configLogs():
    logging.basicConfig(filename='gameLogger.log',  level=logging.DEBUG)

def start_game():
    configLogs()

    tprint("Schere Stein Papier")
    print("Hallo das hier ist ein Schere Stein Papier Spiel")
    print("Es ist ein Super Spiel ")
    ask_player()
  

def ask_player():
    print("Wähle aus :")
    print("[1] Schere")
    print("[2] Stein")
    print("[3] Papier")

    auswahl = input()

    if auswahl == "1":
        auswahlch="Schere"
        conter="Stein"
        conterPC(auswahlch,conter)
    elif auswahl == "2": 
        auswahlch="Stein"
        conter="Papier"
        conterPC(auswahlch,conter)
    elif auswahl == "3":
        auswahlch="Papier"
        conter="Schere"
        conterPC(auswahlch,conter)

def conterPC(auswahl,conter):
    print("Du hast "+auswahl+" gewählt ist wähle "+conter)
    print("Nochmal ? :) ")
    print("y/n ?")

    yes_no=input()
    if yes_no == "y":
        ask_player()
        logging.warning("User have try again")
    else:
        print("loooossser")
        logging.info("user have loser the game ")


start_game()
