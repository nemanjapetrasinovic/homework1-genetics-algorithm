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

    def ukrstanje(self, konfiguracijaA, konfiguracijaB, novaPopulacija):
        pozCepanja = random.randint(1, 7)
        array = [a for a in dir(konfiguracijaA) if not a.startswith('__') and not callable(getattr(konfiguracijaA, a))]
        
        for i in range(pozCepanja, array.__len__()):
            pom = getattr(konfiguracijaA, array[i])
            setattr(konfiguracijaA, array[i], getattr(konfiguracijaB, array[i]))
            setattr(konfiguracijaB, array[i], pom)
        
        konfiguracijaA.racunajCenu()
        konfiguracijaB.racunajCenu()

        novaPopulacija.append(konfiguracijaA)
        novaPopulacija.append(konfiguracijaB)

    def mutacija(self, konfiguracija, procesori, maticnePloce, grafickeKartice, ramMemorije, storage, napajanja, optickiUredjaji):
        verovatnoce = [random.random() for _ in xrange(7)]
        
        if verovatnoce[0] > 0.5:
            konfiguracija.grafickaKartica = grafickeKartice[random.randint(0, 4)]
        if verovatnoce[1] > 0.5:
            konfiguracija.maticnaPloca = maticnePloce[random.randint(0, 4)]
        if verovatnoce[2] > 0.5:
            konfiguracija.napajanje = napajanja[random.randint(0, 4)]
        if verovatnoce[3] > 0.5:
            konfiguracija.optickiUredjaj = optickiUredjaji[random.randint(0, 4)]
        if verovatnoce[4] > 0.5:
            konfiguracija.procesor = procesori[random.randint(0, 4)]
        if verovatnoce[5] > 0.5:
            konfiguracija.ramMemorija = ramMemorije[random.randint(0, 4)]
        if verovatnoce[6] > 0.5:
            konfiguracija.storage = storage[random.randint(0, 4)]
        
        konfiguracija.racunajCenu()