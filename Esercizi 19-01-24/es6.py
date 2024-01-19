#definisco una classe alunno
#aggiungo degli attributi


class alunno:
    def __init__(self, nome, cognome, età, corso, fuoricorso=False):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.corso = corso
        self.fuoricorso = fuoricorso

    def mora(self):
        if self.fuoricorso == True:
            print("In regola")

        else:
            print("Devi pagare una mora")



marta = alunno("marta", "bignani", 30, "Inglese", True)
simona = alunno("simona", "passeri", 28, "Spagnolo")

#uso della funziona mora() manuale
marta.mora()
simona.mora()

#creo una lista con tutti gli studenti
studenti = [marta, simona]

#uso della funzione mora() col ciclo for
for studente in studenti:
    studente.mora()