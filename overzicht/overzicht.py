__author__ = 'gebruiker'

import datetime
from database import *

def save_to_file(bestand):
    datum = datetime.date.today()
    tijd = datetime.datetime.today().time().strftime('%H-%M-%S')

    with open("Rapport " + str(datum) + " " + str(tijd) + ".txt", "w") as text_file:
        for row in bestand:
            text_file.write(row)

bestand = []

#aantal reizen per ov chipkaart
query = database.query("SELECT COUNT(*),ovnummer FROM reisgegevens JOIN gebruikers ON(gebruikers.gebruikerID = reisgegevens.gebruikerID) GROUP BY reisgegevens.gebruikerID")

aantal_reizen_per_ov = database.fetchAll(query)

bestand.append("\nAantal reizen per OVnummer\n")
bestand.append('{:<14}  {:<12}\n'.format("Aantal reizen", "Ovnummer"))
for row in aantal_reizen_per_ov:
    bestand.append('{:<14}  {:<12}\n'.format(row[0],row[1]))


#populairste bestemming
query = database.query("SELECT stations.naam, count(eindstationID) FROM reisgegevens JOIN stations ON(reisgegevens.eindstationID = stationID) GROUP BY eindstationID ORDER BY count(eindstationID) desc LIMIT 5")

populairste_bestemmingen = database.fetchAll(query)

bestand.append("\nPopulairste 5 bestemmingen\n")
bestand.append('{:<20}  {:<12}\n'.format("Bestemming", "Hoevaak als eindbestemming"))


for row in populairste_bestemmingen:
    bestand.append('{:<20}  {:<12}\n'.format(row[0],row[1]))


#populairste vertrekstation
query = database.query("SELECT stations.naam, count(beginstationID) FROM reisgegevens JOIN stations ON(reisgegevens.beginstationID = stationID) GROUP BY beginstationID ORDER BY count(beginstationID) desc LIMIT 5")

populairste_vertrekstations = database.fetchAll(query)

bestand.append("\nPopulairste 5 vertrekstations\n")
bestand.append('{:<20}  {:<12}\n'.format("Station", "Hoevaak als vertrekstation"))

for row in populairste_vertrekstations:
    bestand.append('{:<20}  {:<12}\n'.format(row[0],row[1]))

save_to_file(bestand)