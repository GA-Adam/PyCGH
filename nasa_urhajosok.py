def fajl_beolvasasa():
    with open('astronauts.csv', 'r') as forrasfajl:
        szoveg = forrasfajl.readlines()
    return szoveg


def szuletes(szoveg):
    szuletesi_datumok = []
    for sor in szoveg[1:]:
        adatok = sor.strip().split(',')
        szuletesi_datumok.append(adatok[4])
    return szuletesi_datumok


def leggyakoribb_szuletesi_honapok(szuletesi_datumok):
    honapok = []
    honapszamok = []
    leggyakoribb_honapok = []
    for datum in szuletesi_datumok:
        honap = datum.split('/')[0]
        honapok.append(honap)
    lista_hossza = len(honapok)
    for _ in range(3):
        honapszam = 0
        leggyakoribb_honap = max(set(honapok), key=honapok.count)
        leggyakoribb_honapok.append(leggyakoribb_honap)
        for _ in honapok:
            if leggyakoribb_honap in honapok:
                honapszam += 1
                honapok.remove(leggyakoribb_honap)
        honapszamok.append(honapszam)
    return lista_hossza, honapszamok, leggyakoribb_honapok


def szazalekszamitas_es_kerekites(szukseges):
    i = 0
    szazalekos_aranyok = []
    for _ in range(3):
        szazalekos_arany = round(szukseges[1][i] / szukseges[0] * 100, 1)
        szazalekos_aranyok.append(szazalekos_arany)
        i = i + 1
    return szazalekos_aranyok


def kiiras(szukseges, szazalekos_aranyok):
    i = 1
    for _ in range(3):
        print(f'A(z) {i}. leggyakoribb születési hónap a {szukseges[2][i - 1]}. hónap,'
              f' {szazalekos_aranyok[i - 1]} %-os aránnyal.')
        i = i + 1


def main():
    szoveg = fajl_beolvasasa()
    szuletesi_datumok = szuletes(szoveg)
    szukseges = leggyakoribb_szuletesi_honapok(szuletesi_datumok)
    szazalekos_aranyok = szazalekszamitas_es_kerekites(szukseges)
    kiiras(szukseges, szazalekos_aranyok)


main()
