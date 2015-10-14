__author__ = 'gebruiker'

from database import *


#aantal reizen per ov chipkaart
query = database.query("SELECT COUNT(*),ovnummer FROM reisgegevens JOIN gebruikers ON(gebruikers.gebruikerID = reisgegevens.gebruikerID) GROUP BY reisgegevens.gebruikerID")

aantal_reizen_per_ov = query.fetchall()

print("Aantal reizen per OVnummer\n")
print('{:<14}  {:<12}'.format("Aantal reizen", "Ovnummer"))
for row in aantal_reizen_per_ov:
    print('{:<14}  {:<12}'.format(row[0],row[1]))


#populairste bestemming
query = database.query("SELECT stations.naam, count(eindstationID) FROM reisgegevens JOIN stations ON(reisgegevens.eindstationID = stationID) GROUP BY eindstationID ORDER BY count(eindstationID) desc LIMIT 5")

populairste_bestemmingen = query.fetchall()

print("\nPopulairste 5 bestemmingen\n")
print('{:<20}  {:<12}'.format("Bestemming", "Hoevaak als eindbestemming"))


for row in populairste_bestemmingen:
    print('{:<20}  {:<12}'.format(row[0],row[1]))


#populairste vertrekstation
query = database.query("SELECT stations.naam, count(beginstationID) FROM reisgegevens JOIN stations ON(reisgegevens.beginstationID = stationID) GROUP BY beginstationID ORDER BY count(beginstationID) desc LIMIT 5")

populairste_vertrekstations = query.fetchall()

print("\nPopulairste 5 vertrekstations\n")
print('{:<20}  {:<12}'.format("Station", "Hoevaak als vertrekstation"))

for row in populairste_vertrekstations:
    print('{:<20}  {:<12}'.format(row[0],row[1]))