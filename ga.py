import random
from konfiguracija import Konfiguracija


class GAlgoritam:

    def RandomKonfiguracija(self, maticnePloce, procesori, grafickeKartice, ramMemorije, storage, napajanja, optickiUredjaji):
        return Konfiguracija(maticnePloce[random.randint(1, 5)],
                             procesori[random.randint(1, 5)],
                             grafickeKartice[random.randint(1, 5)],
                             ramMemorije[random.randint(1, 5)],
                             storage[random.randint(1, 5)],
                             napajanja[random.randint(1, 5)],
                             optickiUredjaji[random.randint(1, 5)])
