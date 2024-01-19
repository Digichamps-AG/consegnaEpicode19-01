#Crea una classe Persona con attributi come nome, cognome e età. Inserisci un metodo per stampare le informazioni della persona.

class persona:
    def __init__(self, nome, cognome, età):
        self.nome = nome
        self.cognome = cognome
        self.età = età

    def stampaInfo(self):
        return print(self.nome, self.cognome, self.età, sep=", ")

personaggio = persona("Archimede", "Pitagorico", 45)
personaggio.stampaInfo()

