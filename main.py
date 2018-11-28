from komponente import Procesor
from komponente import MaticnaPloca
from komponente import GrafickaKartica
from komponente import RAM
from komponente import HDD
from komponente import Napajanje
from komponente import OptickiUredjaj
from konfiguracija import Konfiguracija
from ga import GAlgoritam
import dataProvider
import random


procesori = []
maticnePloce = []
grafickeKartice = []
ramMemorije = []
storage = []
napajanja = []
optika = []

procesori = dataProvider.dodajProcesore()
maticnePloce = dataProvider.dodajMaticnePloce()
grafickeKartice = dataProvider.dodajGrafickeKartice()
ramMemorije = dataProvider.dodajRAM()
storage = dataProvider.dodajStorage()
napajanja = dataProvider.dodajNapajanja()
optickiUredjaji = dataProvider.dodajOpticeUredjaje()

'#Izvrsavanje algoritma'

ga = GAlgoritam()

populacija = []
novaPopulacija = []

for x in range(50):
    k = ga.RandomKonfiguracija(maticnePloce, procesori, grafickeKartice, ramMemorije, storage, napajanja, optickiUredjaji)
    populacija.append(k)
    populacija.sort(key=Konfiguracija.fittnes, reverse=True)

while populacija[0].fittnes() < 6:
    for i in range(25):
        ga.ukrstanje(populacija[random.randint(0, 49)], populacija[random.randint(0, 49)], novaPopulacija)
    
    populacija = novaPopulacija
    
    for i in range(50):
        ga.mutacija(populacija[i], procesori, maticnePloce, grafickeKartice, ramMemorije, storage, napajanja, optickiUredjaji)
    
    populacija.sort(key=Konfiguracija.fittnes, reverse=True)
    novaPopulacija = []

populacija[0].stampaj()
