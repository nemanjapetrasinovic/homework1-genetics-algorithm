from komponente import Procesor
from komponente import MaticnaPloca
from komponente import GrafickaKartica
from komponente import RAM
from komponente import HDD
from komponente import Napajanje
from komponente import OptickiUredjaj


def dodajProcesore():
    procesori = []
    p = Procesor("Intel", 4, 8, "7nm", "3.2 GHz", "2 MB", 15000)
    procesori.append(p)

    p = Procesor("AMD", 4, 4, "14nm", "3.1 GHz", "2 MB", 11999)
    procesori.append(p)

    p = Procesor("Intel", 2, 2, "14nm", "3.3 GHz", "512 KB", 10999)
    procesori.append(p)

    p = Procesor("AMD", 8, 16, "14 nm", "3.6 GHz", "2 MB", 33999)
    procesori.append(p)

    p = Procesor("Intel", 4, 4, "14 nm", "3,4 GHz", "6 MB", 33999)
    procesori.append(p)

    return procesori


def dodajMaticnePloce():
    maticnePloce = []

    m = MaticnaPloca("Intel", "Micro ATX", "Asus", "DDR3", "AMD Radeon 2048 MB", 6799)
    maticnePloce.append(m)

    m = MaticnaPloca("AMD", "Micro ATX", "ASRock", "DDR3", "AMD Radeon 2048 MB", 6699)
    maticnePloce.append(m)

    m = MaticnaPloca("AMD", "ATX", "Asus", "DDR4", "AMD Ryzen 2048 MB", 21999)
    maticnePloce.append(m)

    m = MaticnaPloca("Intel", "ATX", "GIGABYTE", "DDR4", "Intel HD 1024 MB", 20999)
    maticnePloce.append(m)

    m = MaticnaPloca("Intel", "ATX", "Asus", "DDR4", "Processor GPU", 19999)
    maticnePloce.append(m)

    return maticnePloce


def dodajRAM():
    ramMemorije = []

    ram = RAM("Kingston", "DDR3", 2, 1333, 1.5, 2499)
    ramMemorije.append(ram)

    ram = RAM("Kingston", "DDR4", 4, 2400, 1.2, 5499)
    ramMemorije.append(ram)

    ram = RAM("Transcend", "DDR4", 8, 2400, 1.2, 8499)
    ramMemorije.append(ram)

    ram = RAM("Kingston", "DDR4", 16, 2400, 1.2, 19999)
    ramMemorije.append(ram)

    ram = RAM("Kingston", "DDR4", 16, 2400, 1.2, 19999)
    ramMemorije.append(ram)

    return ramMemorije


def dodajStorage():
    storage = []

    hdd = HDD("Toshiba", "Interni", 3.5, "500 GB", "SATA III", 7200, 64, 5499)
    storage.append(hdd)

    hdd = HDD("Seagate", "Interni", 3.5, "1 TB", "SATA III", 7200, 64, 5499)
    storage.append(hdd)

    hdd = HDD("Western Digital", "Interni", 3.5, "1 TB", "SATA III", 7200, 64, 10499)
    storage.append(hdd)

    hdd = HDD("Toshiba", "Interni", 3.5, "2 TB", "SATA III", 7200, 64, 10499)
    storage.append(hdd)

    hdd = HDD("Western Digital", "Interni", 3.5, "6 TB", "SATA III", 7200, 64, 25999)
    storage.append(hdd)

    return storage


def dodajGrafickeKartice():
    grafickeKartice = []

    gr = GrafickaKartica("Asus", "GDDR5", "1 GB", "AMD Radeon R5 230", 64, 1200, 5199)
    grafickeKartice.append(gr)

    gr = GrafickaKartica("GIGABYTE", "GDDR3", "1 GB", "Nvidia GeForce GT 710", 64, 1600, 5599)
    grafickeKartice.append(gr)

    gr = GrafickaKartica("MSI", "GDDR5", "2 GB", "Nvidia GeForce GTX 1050", 128, 7008, 19999)
    grafickeKartice.append(gr)

    gr = GrafickaKartica("Asus", "GDDR5", "4 GB", "AMD Radeon RX 560", 128, 6000, 20999)
    grafickeKartice.append(gr)

    gr = GrafickaKartica("MSI", "GDDR5", "3 GB", "Nvidia GeForce GTX 1060", 192, 8008, 37999)
    grafickeKartice.append(gr)
    return grafickeKartice


def dodajNapajanja():
    napajanja = []

    n = Napajanje("MS Industrial", "Standardno ATX", 500, 3799)
    napajanja.append(n)

    n = Napajanje("COOLER MASTER", "Standardno ATX", 600, 8499)
    napajanja.append(n)

    n = Napajanje("COOLER MASTER", "Modularno ATX", 1200, 42999)
    napajanja.append(n)

    n = Napajanje("GIGABYTE", "Semi-Modularno ATX", 700, 9999)
    napajanja.append(n)

    n = Napajanje("THERMALTAKE", "Semi-Modularno ATX", 730, 12499)
    napajanja.append(n)

    return napajanja


def dodajOpticeUredjaje():
    optickiUredjaji = []

    o = OptickiUredjaj("LG", "Interni", "DVD rezac", 1999)
    optickiUredjaji.append(o)

    o = OptickiUredjaj("Asus", "Interni", "DVD rezac", 1999)
    optickiUredjaji.append(o)

    o = OptickiUredjaj("LG", "Interni", "Blu-ray rezac", 9999)
    optickiUredjaji.append(o)

    o = OptickiUredjaj("LG", "Portable", "DVD rezac", 3999)
    optickiUredjaji.append(o)

    o = OptickiUredjaj("Asus", "Eksterni", "DVD rezac", 4499)
    optickiUredjaji.append(o)

    return optickiUredjaji
