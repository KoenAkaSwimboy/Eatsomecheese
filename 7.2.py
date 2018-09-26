infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
for regel in regels:
    zin = regel.split(' ')

    nummer = zin[0]
    nummer = nummer.strip(',')

    voornaam = zin[1]

    achternaam = zin[2]
    if len(zin) >3:
        achternaam = achternaam + ' ' + zin[3]
    achternaam = achternaam.strip('\n')

    print(voornaam, achternaam, 'heeft klantnummer: ', nummer)