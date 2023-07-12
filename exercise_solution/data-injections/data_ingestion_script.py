import csv
import mysql.connector
import os
from dotenv import load_dotenv

# # Read the configuration file
load_dotenv('config.env')

# MySQL database connection details
db_config = {
    'host': os.environ['MYSQL_HOST'],
    'user': os.environ['MYSQL_USER'],
    'password': os.environ['MYSQL_PASSWORD'],
    'database': os.environ['MYSQL_DATABASE']
}

# Read and load places.csv
with open('data/places.csv', 'r', encoding="utf-8") as places_file:
    places_data = csv.DictReader(places_file)
    
    # Connect to the MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insert each row into the places table
    for row in places_data:
        query = "INSERT INTO places (city, county, country) VALUES (%s, %s, %s)"
        values = (row['city'], row['county'], row['country'])
        cursor.execute(query, values)

    # Commit the changes and close the cursor and connection
    conn.commit()
    cursor.close()
    conn.close()

# Read and load people.csv
with open('data/people.csv', 'r', encoding="utf-8") as people_file:
    people_data = csv.DictReader(people_file)
    
    # Connect to the MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insert each row into the people table
    for row in people_data:
        query = "INSERT INTO people (given_name, family_name, date_of_birth, place_of_birth) VALUES (%s, %s, %s, %s)"
        values = (row['given_name'], row['family_name'], row['date_of_birth'], row['place_of_birth'])
        cursor.execute(query, values)

    # Commit the changes and close the cursor and connection
    conn.commit()
    cursor.close()
    conn.close()