'''Creazione di una classe Cerchio: 
Definisci una classe Cerchio con un attributo raggio e metodi per calcolare l'area e la circonferenza.'''

class cerchio:
    def __init__(self, raggio):
        self.raggio = raggio

    def calcoloArea(self):
        p = 3.14
        return p * (self.raggio)**2
    
    def calcoloCirconferenza(self):
        p = 3.14
        return p * (self.raggio)*2
    
tondo = cerchio(5)
print(tondo.calcoloArea())
print(tondo.calcoloCirconferenza())