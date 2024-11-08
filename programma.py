scelta = 1
somma = 0

while scelta != 0:
    scelta = int(input("Inserisci un numero (zero per terminare): "))
    somma += scelta
print(f"La somma di tutti i numeri è {somma}")