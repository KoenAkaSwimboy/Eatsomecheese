afstandKM = int(input( 'Hoeveel kilometer gaat u reizen:'))
leeftijd = int(input('Hoe oud bent u:'))
dag = input('Reist u doordeweeks of in het weekend:')


def standaardprijs(afstandKM):

    if afstandKM < 0:
        return (0)

    elif afstandKM <= 50:
        return(0.8 * afstandKM)



    else:
        return(afstandKM * 0.6 + 15)


def ritprijs(afstandKM, leeftijd, dag):
    if (leeftijd <= 12 or leeftijd >= 65) and (dag == 'weekend'):
        return(standaardprijs(afstandKM)) * 0.65

    elif (leeftijd <= 12 or leeftijd >= 65) and (dag != 'weekend'):
         return(standaardprijs(afstandKM)) * 0.70

    elif (leeftijd >= 12 or leeftijd <= 65) and (dag == 'weekend'):
        return(standaardprijs(afstandKM)) * 0.60
    else:
        return(standaardprijs(afstandKM))



print('€', round(ritprijs(afstandKM, leeftijd, dag), 2))