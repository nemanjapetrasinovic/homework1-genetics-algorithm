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
