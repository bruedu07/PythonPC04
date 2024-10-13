import requests

url = "https://raw.githubusercontent.com/gdelgador/ProgramacionPython202407/main/Modulo4/src/temperaturas.txt"
response = requests.get(url)
with open("temperaturas.txt", "wb") as f:
    f.write(response.content)

temperaturas = []

with open("temperaturas.txt", "r") as f:
    for linea in f:
        # Separar la fecha y la temperatura
        fecha, temp = linea.strip().split(',')
        # Convertir la temperatura a float y agregarla a la lista
        temperaturas.append(float(temp))

temperatura_promedio = sum(temperaturas) / len(temperaturas)
temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)

with open("resumen_temperaturas.txt", "w") as f:
    f.write(f"Temperatura Promedio: {temperatura_promedio:.2f}\n")
    f.write(f"Temperatura Máxima: {temperatura_maxima:.2f}\n")
    f.write(f"Temperatura Mínima: {temperatura_minima:.2f}\n")

print("Resultados escritos en 'resumen_temperaturas.txt'.")
