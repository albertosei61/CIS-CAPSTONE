from flask import Flask, render_template, request, jsonify
#from geopy.geocoders import Nominatim
import sqlite3
import requests
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    location = request.form.get('location')

    if username is not None and location is not None:
        timestamp = datetime.now()
        # URL for the Google Maps Geocoding API
        API_KEY = os.getenv('API_KEY_CIS_Google_Maps_API')
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={API_KEY}"

        # Send a GET request to the API
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'OK':
            result = data['results'][0]
            location_info = result.get('geometry', {}).get('location', {})
            formatted_address = result.get('formatted_address', '')
            latitude = location_info.get('lat', None)
            longitude = location_info.get('lng', None)

            if latitude is not None and longitude is not None:
                conn = sqlite3.connect('user_data.db')
                cursor = conn.cursor()

                cursor.execute('''
                    INSERT INTO user_info (username, location, latitude, longitude, timestamp)
                    VALUES (?, ?, ?, ?, ?)
                ''', (username, formatted_address, latitude, longitude, timestamp))

                conn.commit()

                #Second Data Base

                conn1 = sqlite3.connect('weather_data.db')  # replace 'second_database.db' with your second database name
                cursor1 = conn1.cursor()

    # Query the second database and retrieve the data
                cursor1.execute('SELECT * FROM weather_data')  # replace 'second_table' with your table name in the second database
                data1 = cursor1.fetchall()

    # Print the retrieved data from the second database
                for row in data1:
                    print(row)

                # Close the second database connection
                conn1.close()


                conn.close()

                return render_template('index.html')
            else:
                print("Latitude or Longitude not found in the response.")

        else:
            print(f"Geocoding failed for {location}")

        return render_template('index.html')  # or an error page
    else:
        return jsonify({'error': 'Missing data'})
    
@app.route('/get_data', methods=['POST'])
def get_data():
    record_id = request.form.get('id')

    # Step 1: Connect to the SQLite database
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    conn1 = sqlite3.connect('weather_data.db')
    cursor1 = conn1.cursor()

    # Step 2: Execute a SELECT query
    query = "SELECT * FROM user_info WHERE id = ?"
    cursor.execute(query, (record_id))

    query = "SELECT * FROM weather_data WHERE id = ?"

    # Step 3: Fetch the results
    data = cursor.fetchone()



    # Step 4: Create an HTML page with the fetched data
    
    if data:
        record = {
            'id': data[0],
            'name': data[1],
            'location': data[2],
            'longitude': data[3],
            'latitude': data[4],
            'timestamp': data[5],
            'weather': data[0],
            'temperature': data[2]
        }
        return render_template('show_data.html', record=record)
    else:
        return "Record not found"

    conn.close()

if __name__ == '__main__':
    app.run(debug=True)