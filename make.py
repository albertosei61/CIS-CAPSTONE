import requests
import sys
import sqlite3
from datetime import datetime
import os

#API key and base URL
API_KEY = os.getenv('API_KEY_CIS_CAPSTONE')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data["main"]["temp"] * 9/5 - 459.67, 2)  # Convert from Kelvin to Fahrenheit
        return weather, temperature
    else:
        return None, None

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('user_data.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the user_info table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        location TEXT,
        latitude REAL,
        longitude REAL,
        timestamp TEXT
    )
''')

# Create the weather_data table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        city TEXT,
        weather TEXT,
        temperature REAL
    )
''')

# Example data to be inserted into the user_info table
user_data = ('JohnDoe', 'New York', 40.7128, -74.0060, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Insert data into the user_info table
cursor.execute('''
    INSERT INTO user_info (username, location, latitude, longitude, timestamp)
    VALUES (?, ?, ?, ?, ?)
''', user_data)

address = input("Enter a city name: ")
if "," in address:
    city = address.split(",")[1].strip()
else:
    city = address.strip()

weather, temperature = get_weather(city)

if weather is not None and temperature is not None:
    # Insert data
    cursor.execute("INSERT INTO weather_data (city, weather, temperature) VALUES (?, ?, ?)", (city, weather, temperature))
    conn.commit()

    print("Weather:", weather)
    print("Temperature:", temperature, "Fahrenheit")

else:
    print("An error occurred.")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and tables created, and data inserted successfully.")
