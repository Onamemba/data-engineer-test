import json
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
# Connect to the MySQL database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Query to retrieve the summary information
query = """
    SELECT p.place_of_birth AS country, COUNT(*) AS count
    FROM people p
    GROUP BY p.place_of_birth
"""

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Convert the results to a list of dictionaries
summary_data = [{'country': country, 'count': count} for (country, count) in results]

# Close the cursor and connection
cursor.close()
conn.close()

# Write the summary data to a JSON file
output_file = 'data/summary_output.json'
with open(output_file, 'w') as file:
    json.dump(summary_data, file, indent=4)

print(f'Summary output saved to {output_file}')