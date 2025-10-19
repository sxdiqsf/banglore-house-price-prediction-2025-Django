import csv
from application.models import *

def run():
    with open('house_prices_bangalore.csv',newline='',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            House.objects.create(
                area = int(row['area']),
                location = row['location'],
                bhk = int(row['bhk']),
                bath = int(row['bath']),
                balcony = int(row['balcony']),
                parking = int(row['parking']),
                furnishing = row['furnishing'],
                property_type = row['property_type'],
                age = int(row['age']),
                price = float(row['price'])
            )
            print(row)
    
    print("successfull")