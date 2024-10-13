import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        precio_usd = data['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException:
        return None

try:
    n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
except ValueError:
    print("Debe ingresar un número válido.")
    exit()

precio_bitcoin = obtener_precio_bitcoin()

if precio_bitcoin is not None:
    total = n * precio_bitcoin
    print(f"El valor de {n} Bitcoins en USD es: ${total:,.4f}")
else:
    print("No se pudo obtener el precio actual de Bitcoin.")
