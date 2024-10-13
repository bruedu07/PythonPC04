import random
from pyfiglet import Figlet

figlet = Figlet()

fuentes_disponibles = figlet.getFonts()

nombre_fuente = input("Ingrese el nombre de la fuente (deje vacío para seleccionar una aleatoria): ")

if not nombre_fuente:
    nombre_fuente = random.choice(fuentes_disponibles)

figlet.setFont(font=nombre_fuente)

texto = input("Ingrese el texto que desea imprimir: ")

print(figlet.renderText(texto))

