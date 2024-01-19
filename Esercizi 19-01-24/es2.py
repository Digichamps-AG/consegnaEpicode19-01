'''Gestione di una classe Libro: 
Creare una classe Libro 
con attributi come titolo, autore e anno di pubblicazione. 
Aggiungi un metodo per verificare se il libro è recente.'''

class libro:
    def __init__(self, titolo, autore, anno):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno

    def recente(self):
        if self.anno <1950:
            print("Il libro è vecchio")
        else:
            print("Il libro è recente")

    def titoloLibro(self):
        print(self.titolo)

#libro recente
RP1 = libro("Ready Player One", "Boh", 2000)
RP1.titoloLibro()
RP1.recente()

print()

#libro vecchio
PM = libro("Promessi Sposi", "Manzoni", 1825)
PM.titoloLibro()
PM.recente()
