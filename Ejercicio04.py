import requests

url = "https://github.com/gdelgador/ProgramacionPython202407/blob/main/Modulo4/src/temperaturas.txt"
response = requests.get(url)
with open("temperaturas.txt", "wb") as f:
    f.write(response.content)

temperaturas = []

with open("temperaturas.txt", "r") as f:
    for linea in f:
        linea = linea.strip()
        if linea:
            try:
                fecha, temp = linea.split(',')
                temperaturas.append(float(temp))
            except ValueError:
                print(f"Error al procesar la línea: {linea}")

if temperaturas:
    temperatura_promedio = sum(temperaturas) / len(temperaturas)
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)

    with open("resumen_temperaturas.txt", "w") as f:
        f.write(f"Temperatura Promedio: {temperatura_promedio:.2f}\n")
        f.write(f"Temperatura Máxima: {temperatura_maxima:.2f}\n")
        f.write(f"Temperatura Mínima: {temperatura_minima:.2f}\n")

    print("Resultados escritos en 'resumen_temperaturas.txt'.")
else:
    print("No se encontraron temperaturas válidas en el archivo.")

