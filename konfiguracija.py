class Konfiguracija:

    def __init__(self, maticnaPloca, procesor, grafickaKartica, ramMemorija, storage, napajanje,
                 optickiUredjaj):
        self.maticnaPloca = maticnaPloca
        self.procesor = procesor
        self.grafickaKartica = grafickaKartica
        self.ramMemorija = ramMemorija
        self.storage = storage
        self.napajanje = napajanje
        self.optickiUredjaj = optickiUredjaj
        self.cena = maticnaPloca.cena + procesor.cena + grafickaKartica.cena + \
            ramMemorija.cena + storage.cena + napajanje.cena + optickiUredjaj.cena

    def fittnes(self):
        ocena = 0
        if self.maticnaPloca.tipProcesora == self.procesor.proizvodjac:
            ocena = ocena + 1
        if self.maticnaPloca.podrzanaMemorija == self.ramMemorija.tip:
            ocena = ocena + 1
        if self.ramMemorija.tip == "DDR4":
            ocena = ocena + 1
        if self.ramMemorija.kapacitet == 16:
            ocena = ocena + 1
        if self.maticnaPloca.cena + self.procesor.cena + self.grafickaKartica.cena + \
            self.ramMemorija.cena + self.storage.cena + self.napajanje.cena + self.optickiUredjaj.cena > 100000:
            ocena = ocena + 1
        if self.procesor.proizvodjac == "AMD":
            ocena = ocena + 1

        return ocena

    def racunajCenu(self):
        self.cena = self.maticnaPloca.cena + self.procesor.cena + self.grafickaKartica.cena + \
            self.ramMemorija.cena + self.storage.cena + self.napajanje.cena + self.optickiUredjaj.cena