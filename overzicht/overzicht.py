__author__ = 'gebruiker'

import sqlite3

database_file = "../reis-database.db"

#aantal reizen per ov chipkaart

def genereer_aantal_reizen_per_ov():
    with sqlite3.connect(database_file) as conn:
        stationlijst = []
        c = conn.cursor()

        c.execute("SELECT COUNT(*),ovnummer FROM reisgegevens JOIN gebruikers ON(gebruikers.gebruikerID = reisgegevens.gebruikerID) GROUP BY reisgegevens.gebruikerID")

        return c.fetchall()

aantal_reizen_per_ov = genereer_aantal_reizen_per_ov()

print("Aantal reizen per OVnummer\n")
print('{:<14}  {:<12}'.format("Aantal reizen", "Ovnummer"))
for row in aantal_reizen_per_ov:
    print('{:<14}  {:<12}'.format(row[0],row[1]))

#populairste bestemming

def haal_populairste_bestemmingen():
    with sqlite3.connect(database_file) as conn:
        c = conn.cursor()

        c.execute("SELECT stations.naam, count(eindstationID) FROM reisgegevens JOIN stations ON(reisgegevens.eindstationID = stationID) GROUP BY eindstationID ORDER BY count(eindstationID) desc LIMIT 5")

        return c.fetchall()

print("\nPopulairste 5 bestemmingen\n")
print('{:<20}  {:<12}'.format("Bestemming", "Hoevaak als eindbestemming"))
populairste_bestemmingen = haal_populairste_bestemmingen()

for row in populairste_bestemmingen:
    print('{:<20}  {:<12}'.format(row[0],row[1]))

#populairste vertrekstation

def haal_populairste_vertrekstations():
    with sqlite3.connect(database_file) as conn:
        stationlijst = []
        c = conn.cursor()

        c.execute("SELECT stations.naam, count(beginstationID) FROM reisgegevens JOIN stations ON(reisgegevens.beginstationID = stationID) GROUP BY beginstationID ORDER BY count(beginstationID) desc LIMIT 5")

        return c.fetchall()

populairste_vertrekstations = haal_populairste_vertrekstations()

print("\nPopulairste 5 vertrekstations\n")
print('{:<20}  {:<12}'.format("Station", "Hoevaak als vertrekstation"))

for row in populairste_vertrekstations:
    print('{:<20}  {:<12}'.format(row[0],row[1]))