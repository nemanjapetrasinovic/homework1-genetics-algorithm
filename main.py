from komponente import Procesor
from komponente import MaticnaPloca
from komponente import GrafickaKartica
from komponente import RAM
from komponente import HDD
from komponente import Napajanje
from komponente import OptickiUredjaj
from konfiguracija import Konfiguracija


procesori = []
maticnePloce = []
grafickeKartice = []
ramMemorije = []
storage = []
napajanja = []
optika = []

p = Procesor("Intel", 4, 8, "7nm", "3.2 GHz", "2 MB", 15000)
procesori.append(p)

m = MaticnaPloca("Asus", "MicroATX", "DDR4", "AmdRadeon R", 20000)
maticnePloce.append(m)

gr = GrafickaKartica("Nvidia", "GDDR5", 4, "GTX 1050 Ti", 128, 7008, 25000)
grafickeKartice.append(gr)

ram = RAM("Kingston", "DDR3", 2, 1333, 1.5, 2499)
ramMemorije.append(ram)

hdd = HDD("Toshiba", "Interni", "3.5", 1, "Sata III", 7200, 32, 5999)
storage.append(hdd)

n = Napajanje("Cooler Master", "Standardno", 600, 5000)
napajanja.append(n)

op = OptickiUredjaj("Asus", "Interni", "DVD - RW", 2999)
optika.append(op)

k = Konfiguracija(m, p, gr, ram, hdd, n, op)