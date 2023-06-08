import sqlite3
from datetime import datetime, timedelta
from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the database connection parameters
database = 'database.db'

# Define the API endpoint that will retrieve the average energy production and consumption data
@app.route('/energy-data/average', methods=['GET'])
def get_average_energy_data():
    # Parse the query parameters for start and end dates
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    # Connect to the database
    conn = sqlite3.connect(database)
    # Execute the SQL query and retrieve the data
    cursor = conn.cursor()
    if start_date is None and end_date is None:
        # If no date range is specified, retrieve average data for the last 14 days
        query = """
        SELECT AVG(EnergyProduction), AVG(EnergyConsumption)
        FROM StationStatus
        WHERE Date >= ?
        """
        start_date = datetime.now() - timedelta(days=14)
        start_date = start_date.strftime('%m/%d/%Y')
        cursor.execute(query, (start_date,))
    else:
        # If start and end dates are specified, retrieve average data for the date range
        query = """
        SELECT AVG(EnergyProduction), AVG(EnergyConsumption)
        FROM StationStatus
        WHERE Date BETWEEN ? AND ?
        """
        start_date = datetime.strptime(start_date, '%m/%d/%Y')
        end_date = datetime.strptime(end_date, '%m/%d/%Y')
        cursor.execute(query, (start_date, end_date))
    rows = cursor.fetchall()
    # Transform the data into a dictionary with average values
    data = {
        'average_energy_production': rows[0][0],
        'average_energy_consumption': rows[0][1],
    }
    # Close the database connection
    conn.close()
    # Return the data as a JSON response
    return jsonify(data)

# Define the API endpoint that will retrieve energy consumption data for a specific date range
@app.route('/energy-data/consumption', methods=['GET'])
def get_energy_consumption_data():
    # Parse the query parameters for start and end dates
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    # Connect to the database
    conn = sqlite3.connect(database)
    # Execute the SQL query and retrieve the data
    cursor = conn.cursor()
    query = """
    SELECT Date, EnergyConsumption
    FROM StationStatus
    """
    if start_date and end_date:
        # If start and end dates are specified, add a WHERE clause to the query to filter by date range
        query += """
        WHERE Date BETWEEN ? AND ?
        """
        start_date = datetime.strptime(start_date, '%m/%d/%Y')
        end_date = datetime.strptime(end_date, '%m/%d/%Y')
        cursor.execute(query, (start_date, end_date))
    else:
        cursor.execute(query)
    rows = cursor.fetchall()
    # Transform the data into a list of dictionaries
    data = []
    for row in rows:
        data.append({
            'date': row[0],
            'energy_consumption': row[1],
        })
    # Close the database connection
    conn.close()
    # Return the data as a JSON response
    return jsonify(data)

# Define the API endpoint that will retrieve energy production data for a specific date range
@app.route('/energy-data/production', methods=['GET'])
def get_energy_production_data():
    # Parse the query parameters for start and end dates
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    # Connect to the database
    conn = sqlite3.connect(database)
    # Execute the SQL query and retrieve the data
    cursor = conn.cursor()
    query = """
    SELECT Date, EnergyProduction
    FROM StationStatus
    """
    if start_date and end_date:
        # If start and end dates are specified, add a WHERE clause to the query to filter by date range
        query += """
        WHERE Date BETWEEN ? AND ?
        """
        start_date = datetime.strptime(start_date, '%m/%d/%Y')
        end_date = datetime.strptime(end_date, '%m/%d/%Y')
        cursor.execute(query, (start_date, end_date))
    else:
        cursor.execute(query)
    rows = cursor.fetchall()
    # Transform the data into a list of dictionaries
    data = []
    for row in rows:
        data.append({
            'date': row[0],
            'energy_production': row[1],
        })
    # Close the database connection
    conn.close()
    # Return the data as a JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)