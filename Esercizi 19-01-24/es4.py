''' Simulazione di un Conto Bancario: 
Crea una classe ContoBancario 
con attributi saldo e metodo per depositare e prelevare denaro.'''

class contoBancario:
    def __init__(self, saldo):
        self.saldo = saldo
   
    def deposito(self, somma):
        #questa linea di codice modifica il saldo in modo che sia pari al valore iniziale di saldo più la somma inserita (così il saldo rimane aggiornato)
        self.saldo += somma
        return self.saldo

    def prelievo(self, somma):
        #se il saldo è pari a 0:
        if self.saldo == 0:
            print("Non hai fondi")

        #se invece la somma che si cerca di prelevare è maggiore del saldo rimasto:
        elif somma > self.saldo:
            print("Non hai abbastanza soldi")

        #altrimenti aggiorni normalmente il saldo attuale, sottraendo il prelievo
        else:
            self.saldo -= somma

        #mi restituisci il saldo finale
        return self.saldo
    
    def attuale(self):
        print("Il tuo saldo attuale è:", self.saldo, "€")

    
        

mioConto = contoBancario(70)

#controllo il saldo
mioConto.attuale()

#faccio un prelievo
print("Prelevo 20€ e il mio conto va a:", mioConto.prelievo(20))

#faccio un deposito
print("Deposito 50€ e il mio conto va a:", mioConto.deposito(50))

#controllo il saldo
mioConto.attuale()


