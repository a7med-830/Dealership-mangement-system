# database.py
import sqlite3
# from dealership_management_system import *
# from dealership_objects import *

import sqlite3

def connect_to_db():
    conn = sqlite3.connect('dealership.db')
    return conn

# Initialize the database tables
def initialize_database():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Cars (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        brand TEXT,
                        model TEXT,
                        year TEXT,
                        form TEXT,
                        price REAL,
                        availability TEXT
                     )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Bikes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        brand TEXT,
                        model TEXT,
                        year TEXT,
                        price REAL,
                        availability TEXT
                     )''')
    
    
    conn.commit()
    conn.close()

def add_car_to_db(car):
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Cars (brand, model, year, form, price, availability) VALUES (?, ?, ?, ?, ?, ?)',
                   (car.brand, car.model, car.year, car.form, car.price, 'Yes' if car.isAvailable else 'No'))

    conn.commit()
    conn.close()

def fetch_all_cars():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Cars')
    cars = cursor.fetchall()

    conn.close()
    return cars

def delete_car_from_db(id_num):
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM Cars WHERE id = ?', (id_num,))
        conn.commit()
        print(f"Car with ID {id_num} has been deleted.")
    except sqlite3.Error as e:
        print(f"An error occurred while deleting the car: {e}")
    finally:
        conn.close()

def add_bike_to_db(bike):
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Bikes (brand, model, year, price, availability) VALUES (?, ?, ?, ?, ?)',
                   (bike.brand, bike.model, bike.year, bike.price, 'Yes' if bike.isAvailable else 'No'))

    conn.commit()
    conn.close()

def fetch_all_bikes():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Bikes')
    bikes = cursor.fetchall()

    conn.close()
    return bikes

def delete_bike_from_db(id_num):
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM Bikes WHERE id = ?', (id_num,))
        conn.commit()
        print(f"Bike with ID {id_num} has been deleted.")
    except sqlite3.Error as e:
        print(f"An error occurred while deleting the bike: {e}")
    finally:
        conn.close()