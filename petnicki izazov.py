

#level1

devojka_iz_petnice = "Da je ljubav nauka\ndobio bih Nobela\nA da je ljubav knjiga\nuzeo bih NIN-a\n\nDevojke iz Petnice\nredom su pametnice\nA jedna među njima\nsad moje srce ima\n\nŽelim da sam projekat\ni da sam joj u mislima\nmrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima\n\nDevojka iz Petnice\nona meni znači sve\ni kada me se seti\nja hoću da poletim\n\nDevojka iz Petnice\nu koju sam zaljubljen\nsad uči tamo negde\nDa li pamti mene?\n\nHoću da sam tema\nU nečemu što sprema\nMrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima"
mala_devojka = devojka_iz_petnice.lower()
strofe = mala_devojka.split("\n")
prazno = []
for i in strofe:
    reci1 = i.split(' ')
    for x in reci1:
        prazno.append(x)
print(prazno)
print(len(prazno))

neponovljene = set(prazno)
print(neponovljene)
print(len(neponovljene))

#nece zajedno da radi iz nekog razloga :/

#ali...
#level2
devojka_iz_petnice = "Da je ljubav nauka\ndobio bih Nobela\nA da je ljubav knjiga\nuzeo bih NIN-a\n\nDevojke iz Petnice\nredom su pametnice\nA jedna među njima\nsad moje srce ima\n\nŽelim da sam projekat\ni da sam joj u mislima\nmrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima\n\nDevojka iz Petnice\nona meni znači sve\ni kada me se seti\nja hoću da poletim\n\nDevojka iz Petnice\nu koju sam zaljubljen\nsad uči tamo negde\nDa li pamti mene?\n\nHoću da sam tema\nU nečemu što sprema\nMrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima"
mala_devojka = devojka_iz_petnice.lower()
strofe = mala_devojka.split("\n")
prazno = []
for i in strofe:
    reci1 = i.split(' ')
    for x in reci1:
        prazno.append(x)

neponovljene = []     #hint od Koste :)
for rec in prazno:
    if rec not in neponovljene:
        neponovljene.append(rec)


neponovljene.sort()
recnik = {}
for z in neponovljene:
    fr = 0
    for y in prazno:
        if z == y:
            fr = fr + 1
    recnik[z] = fr
for k, v in recnik.items():
    print(k, v)