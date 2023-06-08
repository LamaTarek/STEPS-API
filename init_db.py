import sqlite3
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect('database.db')

# Define the start date and time for the data
start_date = datetime.now() - timedelta(days=14)
start_time = datetime.strptime('12:00:00 PM', '%I:%M:%S %p')

# Define the interval between data points
time_interval = timedelta(minutes=30)

# Loop through 15 days of data and insert a row for each time point
for i in range(15 * 24 * 2):
    # Calculate the date and time for the current data point
    current_date = start_date + timedelta(minutes=i * 30)
    current_time = start_time + timedelta(minutes=i * 30)
    # Define the values for the current row of data
    values = (
        
        '12:30:00', '2023-06-04', 'ABC-123', 25.0, 'Sunny', 10.0, 180.0,
    'Zenith', 45.0, 1000.0, 500.0, 1800000
        
    )
    # Insert the row of data into the StationStatus table
    conn.execute('''
    INSERT INTO StationStatus (
        Time, Date, SystemId, TempDegree, CloudStatus, WindSpeed, WindDirection,
        SunPostion, SolarAngel, EnergyProduction, EnergyConsumption,id
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
    ''', values)

# Commit the changes and close the connection
conn.commit()
conn.close()