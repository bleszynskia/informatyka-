import random

plan = []
wycieczki = []
znane_jezyki = dict()

with open("wycieczki.txt", encoding='utf-8') as plik:
    for line in plik:
        line = line.upper()
        kod, jezyk = line.split()
        wycieczki.append((jezyk,kod))


with open("personel.txt", encoding='utf-8') as plik:
    for line in plik:
        linia = line.upper()
        wyrazy = linia.split()
        imie = wyrazy[0]
        nazwisko = wyrazy[1]
        pracownik = (imie, nazwisko)
        lista_jezykow_znanych = wyrazy[2:]
        for jezyk in lista_jezykow_znanych:
            if jezyk not in znane_jezyki:
                znane_jezyki[jezyk] = set()
            znane_jezyki[jezyk].add(pracownik)


print(wycieczki)
print(znane_jezyki)

znane = znane_jezyki
print(znane)

for w in wycieczki:
    jezyk, kod = w
    if jezyk in znane_jezyki.keys():
        p = random.choice(list(znane[jezyk]))
        znane[jezyk].remove(p)
        plan.append((kod, p))

print(plan)

file = open('plan.txt', 'w+')
for a in plan:
    kod, p = a
    imie, nazwisko = p
    file.write(kod + ' '+ imie+ ' ' +nazwisko +'\n')
