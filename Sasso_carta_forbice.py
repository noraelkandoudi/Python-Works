import random

def sasso_carta_forbice():
    """
    Simula una partita a sasso, carta, forbice tra l'utente e il computer.
    """

    mosse = ["sasso", "carta", "forbice"]

    while True:
        giocatore = input("Scegli: sasso, carta o forbice? ").lower()

        # Verifica se la scelta del giocatore è valida
        if giocatore not in mosse:
            print("Scelta non valida. Riprova.")
            continue

        # Il computer sceglie casualmente una mossa
        computer = random.choice(mosse)

        print(f"Hai scelto {giocatore}, il computer ha scelto {computer}.")

        # Determina il vincitore
        if giocatore == computer:
            print("Pareggio!")
        elif (giocatore == "sasso" and computer == "forbice") or \
             (giocatore == "carta" and computer == "sasso") or \
             (giocatore == un "forbice" and computer == "carta"):
            print("Hai vinto!")
        else:
            print("Hai perso!")

        # Chiede all'utente se vuole continuare a giocare
        giocare_ancora = input("Vuoi giocare ancora? (s/n): ")
        if giocare_ancora.lower() != "s":
            break

# Avvia il gioco
sasso_carta_forbice()