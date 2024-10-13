import requests
import sqlite3
from pymongo import MongoClient

def obtener_tipo_cambio():
    url = "https://api.apis.net.pe/v1/tipocambio"
    tipo_cambio_data = []

    for mes in range(1, 13):
        response = requests.get(f"{url}?anio=2023&mes={mes}")
        if response.status_code == 200:
            data = response.json()
            tipo_cambio_data.extend(data)
        else:
            print(f"Error al obtener datos para 2023-{mes}: {response.status_code}")
    
    return tipo_cambio_data

def almacenar_en_sqlite(data):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT PRIMARY KEY,
            compra REAL,
            venta REAL
        )
    ''')

    for item in data:
        cursor.execute('''
            INSERT OR REPLACE INTO sunat_info (fecha, compra, venta)
            VALUES (?, ?, ?)
        ''', (item['fecha'], item['compra'], item['venta']))

    conn.commit()
    conn.close()
