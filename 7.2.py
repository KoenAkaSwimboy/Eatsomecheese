infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
for regel in regels:
    zin = regel.split(' '), regel.replace('\n', '')
    nummer = zin[0]
    voornaam = zin[1]
    #achternaam = zin[2]
    print(voornaam, 'heeft klantnummer: ')