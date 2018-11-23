import random
from konfiguracija import Konfiguracija


class GAlgoritam:

    def __init__(self):
        pass


    def RandomKonfiguracija(self, maticnePloce, procesori, grafickeKartice, ramMemorije, storage, napajanja, optickiUredjaji):
        return Konfiguracija(maticnePloce[random.randint(0, 4)],
                             procesori[random.randint(0, 4)],
                             grafickeKartice[random.randint(0, 4)],
                             ramMemorije[random.randint(0, 4)],
                             storage[random.randint(0, 4)],
                             napajanja[random.randint(0, 4)],
                             optickiUredjaji[random.randint(0, 4)])
