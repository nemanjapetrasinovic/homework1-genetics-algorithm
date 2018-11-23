from komponente import Procesor
from komponente import MaticnaPloca
from komponente import GrafickaKartica
from komponente import RAM
from komponente import HDD
from komponente import Napajanje
from komponente import OptickiUredjaj
from konfiguracija import Konfiguracija
import dataProvider


procesori = []
maticnePloce = []
grafickeKartice = []
ramMemorije = []
storage = []
napajanja = []
optika = []

procesori = dataProvider.dodajProcesore()
maticnePloce = dataProvider.dodajMaticnePloce()
ramMemorije = dataProvider.dodajRAM()

hdd = HDD("Toshiba", "Interni", "3.5", 1, "Sata III", 7200, 32, 5999)
storage.append(hdd)

n = Napajanje("Cooler Master", "Standardno", 600, 5000)
napajanja.append(n)

op = OptickiUredjaj("Asus", "Interni", "DVD - RW", 2999)
optika.append(op)

#k = Konfiguracija(m, p, gr, ram, hdd, n, op)
