plik = open('liczby.txt', 'r')
tab1 = []
tab2 = [0, 0]
tab3 = []
allNumbers = []
zeroPowtorzen = 0
dwaPowtorzenia = 0
trzyPowtorzenia = 0
najwieksza = 0


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def zad1(n):
    n = n[::-1]
    n = int(n)
    if n % 17 == 0:
        return str(n)
    return False


def zad2(n):
    nReversed = n[::-1]
    n = int(n)
    nReversed = int(nReversed)
    wartosc = abs(n - nReversed)
    return wartosc


def zad3(n):
    nReversed = n[::-1]
    n = int(n)
    nReversed = int(nReversed)
    if isPrime(n) and isPrime(nReversed):
        return True
    return False


for wiersz in plik:
    wiersz = wiersz.strip()
    if zad1(wiersz):
        tab1.append(zad1(wiersz))
    if zad2(wiersz) > tab2[1]:
        tab2.clear()
        tab2.append(wiersz)
        tab2.append(zad2(wiersz))
    if zad3(wiersz):
        tab3.append(wiersz)
    if allNumbers.count(wiersz) == 0:
        zeroPowtorzen += 1
    allNumbers.append(wiersz)
    if int(wiersz) > int(najwieksza):
        najwieksza = int(wiersz)

for x in range(0, najwieksza):
    x = str(x)
    if allNumbers.count(x) == 2:
        dwaPowtorzenia += 1
    if allNumbers.count(x) == 3:
        trzyPowtorzenia += 1

print('## Zad 4.1 ##')
print(" ".join(tab1))
print('## Zad 4.2 ##')
print(tab2[0], tab2[1])
print('## Zad 4.3 ##')
print(" ".join(tab3))
print('## Zad 4.4 ##')
print(zeroPowtorzen, dwaPowtorzenia, trzyPowtorzenia)
