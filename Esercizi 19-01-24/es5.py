'''5. Gestione di una classe Prodotto: 
Crea una classe Prodotto con 
attributi come nome, prezzo e quantità disponibile. 
Aggiungi metodi per calcolare il costo totale e verificare la disponibilità.'''

class prodotto:

    def __init__(self, nome, prezzo, quantDisp):
        self.nome = nome
        self.prezzo = prezzo
        self.quantDisp = quantDisp

    def verificaDisp(self):
        print("La unità disponibili sono:", self.quantDisp)

    def prezzoTot(self):
        print("Il prezzo totale di tutti i fumetti di", self.nome, "in magazzino è:", self.quantDisp*self.prezzo)


fumetti = prodotto("OP", 5.99, 10)
fumetti.verificaDisp()
fumetti.prezzoTot()
