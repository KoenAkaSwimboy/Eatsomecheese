def standaardprijs(afstandKM):

    if 0 < afstandKM < 50:
        return afstandKM * 0.80

    elif afstandKM >= 50:
        return ((afstandKM - 50) * 0.60) + 15

    elif afstandKM <= 0:
        return 0


def ritprijs(leeftijd, weekendrit, afstandKM):

    if leeftijd > 150 or leeftijd < 0:
        return "De ingevoerde leeftijd is ongeldig."

    elif leeftijd < 12 or leeftijd >= 65 and weekendrit == True:
        return standaardprijs(afstandKM) * 0.65

    elif leeftijd < 12 or leeftijd >= 65 and weekendrit == False:
        return standaardprijs(afstandKM) * 0.70

    elif 12 <= leeftijd < 65 and weekendrit == True:
        return standaardprijs(afstandKM) * 0.60

    elif 12 <= leeftijd < 65 and weekendrit == False:
        return standaardprijs(afstandKM)


print(ritprijs(40, False, 50))