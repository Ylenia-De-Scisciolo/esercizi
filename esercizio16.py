nazioni = ["Italia", "Francia", "Germania", "Albania", "Brasile", "Cina", "Croazia", "Estonia", "Georgia"]
capitali = ["Roma", "Parigi", "Berlino", "Tirana", "Brasilia", "Pechino", "Zagabria", "Tallinn", "Tiblisi" ] 

dictionary = {}

#dictionary[key] = value

for i in range(len(nazioni)):
    dictionary[nazioni[i]] = capitali[i]


nazione = input("inserisci nazione")
exist = False

for e in dictionary:
    if nazione == e:
        exist = True

if exist:
    print(dictionary[nazione])

else:
    print("errore")