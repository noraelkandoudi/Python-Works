# Programma per l'utilizzo di generare password


import random
import string

def generate_secure_password(length):
    # Verifica se la lunghezza della password è minore di 8 caratteri
    if length < 8:
        return None

    # Definizione dei caratteri utilizzati per la generazione della password 
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Creazione di una lista di caratteri che contiene almeno un carattere minuscolo
    # uno maiuscolo e un carattere speciale
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    # Aggiunta di caratteri casuali alla lista fino a raggiungere la lunghezza desiderata
    for _ in range(length - 4):
        password.append(random.choice(uppercase_letters + lowercase_letters + digits + special_characters))


    # Mescolamento della lista di caratteri per garantire una password univoca 
    random.shuffle(password)
    password = ''.join(password)

    return password


while True:
    # Richiesta all'utente di inserire la lunghezza della password
    password_length = int(input("\nInserisci la lunghezza che dovrebbe avere la password. (Per una password più sicura inserire dagli 8 caratteri ai 12): "))
    if 8 <= password_length <= 12:
        print("\nPassword generata:", generate_secure_password(password_length))
        break
    else:
        # Messaggio du errore se la lunghezza non è valida
        print("\nUna password sicura dovrebbe avere minimo 8 caratteri. Per favore riprova inserendo una password pai o superiore ad 8 caratteri.")