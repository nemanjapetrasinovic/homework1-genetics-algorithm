class MaticnaPloca:

    def __init__(self, tipProcesora, formatPloce, proizvodjac, podrzanaMemorija, integrisanaGraficka, cena):
        self.tipProcesora = tipProcesora
        self.formatPloce = formatPloce
        self.proizvodjac = proizvodjac
        self.podrzanaMemorija = podrzanaMemorija
        self.integrisanaGraficka = integrisanaGraficka
        self.cena = cena

    def stampaj(self):

        print("Tip procesora: " + self.tipProcesora)
        print("Format ploce: " + self.formatPloce)
        print("Proizvodjac: " + self.proizvodjac)
        print("Podrzana memorija: " + self.podrzanaMemorija)
        print("Inregrisana graficka: " + self.integrisanaGraficka)
        print("Cena: " + self.cena.__str__() + " RSD")


class Procesor:

    def __init__(self, proizvodjac, brojJezgara, threads, tehnologijaIzrade, radnaFerkvencija, kesMemorija, cena):

        self.proizvodjac = proizvodjac
        self.brojJezgara = brojJezgara
        self.threads = threads
        self.tehnologijaIzrade = tehnologijaIzrade
        self.radnaFerkvencija = radnaFerkvencija
        self.kesMemorija = kesMemorija
        self.cena = cena

    def stampaj(self):
        print("Proizvodjac: " + self.proizvodjac)
        print("Broj jezgara: " + self.brojJezgara.__str__())
        print("Threads: " + self.threads.__str__())
        print("Tehnologija izrade: " + self.tehnologijaIzrade)
        print("Radna frekvencija: " + self.radnaFerkvencija)
        print("Kes memorija: " + self.kesMemorija)
        print("Cena: " + self.cena.__str__() + " RSD")


class GrafickaKartica:

    def __init__(self, proizvodjac, tipMemorije, kolicinaMemorije, gpu, magistralaMemorije, brzinaMemorije, cena):

        self.proizvodjac = proizvodjac
        self.tipMemorije = tipMemorije
        self.kolicinaMemorije = kolicinaMemorije
        self.gpu = gpu
        self.magistralaMemorije = magistralaMemorije
        self.brzinaMemorije = brzinaMemorije
        self.cena = cena

    def stampaj(self):

        print("Proizvodjac: " + self.proizvodjac)
        print("Tip memorije: " + self.tipMemorije)
        print("Kolicina memorije: " + self.kolicinaMemorije.__str__() + " GB")
        print("GPU: " + self.gpu)
        print("Magistrala memorije: " +
              self.magistralaMemorije.__str__() + " bitna")
        print("Brzina memorije: " + self.brzinaMemorije.__str__() + " MHz")
        print("Cena: " + self.cena.__str__() + " RSD")


class RAM:

    def __init__(self, proizvodjac, tip, kapacitet, frekvencija, voltaza, cena):

        self.proizvodjac = proizvodjac
        self.tip = tip
        self.kapacitet = kapacitet
        self.frekvencija = frekvencija
        self.voltaza = voltaza
        self.cena = cena

    def stampaj(self):

        print("Proizvodjac: " + self.proizvodjac)
        print("Tip: " + self.tip)
        print("Kapacitet: " + self.kapacitet.__str__() + " MHz")
        print("Frekvencija: " + self.frekvencija.__str__() + " MHz")
        print("Voltaza: " + self.voltaza.__str__() + " V")
        print("Cena: " + self.cena.__str__() + " RSD")


class HDD:

    def __init__(self, proizvodjac, tip, format, kapacitet, konekcija, brojObrtaja, bafer, cena):

        self.proizvodjac = proizvodjac
        self.tip = tip
        self.format = format
        self.kapacitet = kapacitet
        self.konekcija = konekcija
        self.brojObrtaja = brojObrtaja
        self.bafer = bafer
        self.cena = cena

    def stampaj(self):

        print("Proizvodjac: " + self.proizvodjac)
        print("Tip: " + self.tip)
        print("Format: " + self.format.__str__() + "\"")
        print("Kapacitet: " + self.kapacitet)
        print("Konekcija: " + self.konekcija)
        print("Broj obrtaja: " + self.brojObrtaja.__str__() + " RPM")
        print("Bafer: " + self.bafer.__str__() + " MB")
        print("Cena: " + self.cena.__str__() + " RSD")


class Napajanje:

    def __init__(self, proizvodjac, tip, snaga, cena):

        self.proizvodjac = proizvodjac
        self.tip = tip
        self.snaga = snaga
        self.cena = cena

    def stampaj(self):

        print("Proizvodjac: " + self.proizvodjac)
        print("Tip: " + self.tip)
        print("Snaga: " + self.snaga.__str__() + " W")
        print("Cena: " + self.cena.__str__() + " RSD")


class OptickiUredjaj:

    def __init__(self, proizvodjac, tip, vrsta, cena):

        self.proizvodjac = proizvodjac
        self.tip = tip
        self.vrsta = vrsta
        self.cena = cena

    def stampaj(self):

        print("Proizvodjac: " + self.proizvodjac)
        print("Tip: " + self.tip)
        print("Vrsta: " + self.vrsta)
        print("Cena: " + self.cena.__str__() + " RSD")
