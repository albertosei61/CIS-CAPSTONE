import sqlite3

# Connect to the database
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Query the database and retrieve the data
cursor.execute('SELECT * FROM user_info')
data = cursor.fetchall()

# Print the retrieved data
for row in data:
    print(row)

# Close the database connection
conn.close()

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