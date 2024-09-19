              # importeremo casualmente un numero ogni volta che richiamiamo (random)
              # per ottenere un numero casuale intero va definita la funzione 
              # creo un parametro x in modo da poterlo passare a questa 

import random # Importa il modulo 'random' per generare numeri casuali

def guess(x):  # Definisce la funzione 'guess' che prende un argomento 'x'

    random_number = random.randint(1, x) # Genera un numero casuale tra 1 e 'x'
    guess = 0 # Inizializza la variabile 'guess' a 0
              # Continua a chiedere all'utente finchè il numero indovinato non è uguale
              # a 'random_number
    while guess != random_number:  
              # Chiede all'utente di inserire un numero tra 1 e 'x'
        guess = int(input(f'Indovina un numero fra 1 e  {x}: '))
              # Controlla se il numero inserito è minore del numero casuale
        if guess < random_number:
            print("Mi dispiace!, Il numero inserito è troppo basso")
              # Controlla se il numero inserito è maggiore del numero casuale
        elif guess > random_number:
            print("Mi dispiace!Il numero inserito è troppo alto") 
            # Messaggio il numero inserito è troppo alto
              
              # Messaggio di successo quando l'utente indovina il numero corretto
    print(f'Yay! You guessed the number {random_number} correctly!')

# Chiamata alla funzione 'guess' con '10' come argomento 
# L'utente deve indovinare un numero tra 1 e 10
guess(10)
