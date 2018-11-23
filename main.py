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

ga = GAlgoritam()

k = ga.RandomKonfiguracija(maticnePloce, procesori, grafickeKartice, ramMemorije, storage, napajanja, optickiUredjaji)