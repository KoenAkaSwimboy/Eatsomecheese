def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    vrij = 12 - len(regels)
    return print('Er zijn', vrij, 'kluizen vrij')

def nieuwe_kluis():
    Kluizen = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    for regel in regels:
        zin = regel.split(';')
        nummer = zin[0]
        if nummer in Kluizen:
         Kluizen.remove(nummer)

    return print('De Kluizen ', Kluizen, 'zijn nog vrij')

def kluis_openen():
    kluis = input('Geef kluisnummer en wachtwoord (kluisnummer;wachtwoord): ')
    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    for regel in regels:
        zin = regel.split('\n')
        nummer = zin[0]
        if kluis == nummer:
            print('Uw kluis is nu open')
            break
    else:
        print('Kluisnummer of wachtwoord is onjuist')

print('Menu:')
print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
print("2: Ik wil een nieuwe kluis")
print("3: Ik wil even iets uit mijn kluis halen")
print("4: Ik wil stoppen")

while True:
        selection= input("Maak een keuze: ")
        if selection == '1':
            print(toon_aantal_kluizen_vrij())
        elif selection == '2':
            print(nieuwe_kluis())
        elif selection == '3':
            print(kluis_openen())
        elif selection == '4':
            break
        else:
            print('U heeft geen optie aan geklikt!')