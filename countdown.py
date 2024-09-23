# Questo piccolo programma stampa a video un countdown ricevuto in input 
#  dall'utente. Gli ultimi 3 secondi saranno stampati con una colorazione rossa
#  per visualizzare la colorazione rossa suggerisco di installare la libreria
#  colorama (pip3 install colorama dal terminale).



import sys
from time import sleep      # Importo la funzione sleep dal modulo time
import colorama             # Importo il modulo colorama per gestire i colori 
from colorama import Fore, Style

colorama.init()  # Initialize colorama per abilitare i colori 

def countdown(seconds): # Definisce la funzione countdown che prende l'argomento seconds

    while seconds > -1: # Ciclo while che continua fino a quando seconds non sarà 
                        # maggiore di -1  
        mins, secs = divmod(seconds, 60) # Calcola i minuti-secondi rimanenti
        formatted_time = f"{mins:02d}:{secs:02d}" # Formatta il tempo in mm:ss
        if seconds > 3:
            print(formatted_time, end="\r")
        else:
            print(f"{Fore.RED}{formatted_time}{Style.RESET_ALL}", end="\r")  # Stampa il tempo 
                                                                             # formattato in rosso
        sleep(1)    
        seconds -= 1 # Decrementa il conteggio dei secondi 
    print("Countdown Completato !\n") # Stampa il messaggio di fine countdown

user_input = int(input("\nInserisci il numero dalla quale vuoi far partire il countdown: ")) # Input inserito dall'utente
countdown(user_input) # Chiama la funzione countdown con l'input dell'utente
