class Konfiguracija:
    def __init__(self, maticnaPloca, procesor, grafickaKartica, ramMemorija, storage, napajanje,
                 optickuUredjaj):
        self.maticnaPloca = maticnaPloca
        self.procesor = procesor
        self.grafickaKartica = grafickaKartica
        self.ramMemorija = ramMemorija
        self.storage = storage
        self.napajanje = napajanje
        self.optickuUredjaj = optickuUredjaj
        self.cena = maticnaPloca.cena + procesor.cena + grafickaKartica.cena + \
            ramMemorija.cena + storage.cena + napajanje.cena + optickuUredjaj.cena
