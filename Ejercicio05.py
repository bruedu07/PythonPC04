def crear_tabla_multiplicar(n):
    """Crea un archivo con la tabla de multiplicar del número n."""
    with open(f"tabla-{n}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar de {n} guardada en 'tabla-{n}.txt'.")


def leer_tabla_multiplicar(n):
    """Lee y muestra la tabla de multiplicar del número n desde el archivo."""
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            print(f"Tabla de multiplicar de {n}:")
            print(f.read())
    except FileNotFoundError:
        print(f"El archivo 'tabla-{n}.txt' no existe.")


def mostrar_linea_tabla(n, m):
    """Muestra la línea m de la tabla de multiplicar del número n desde el archivo."""
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            lineas = f.readlines()
            if 1 <= m <= len(lineas):
                print(lineas[m - 1].strip())
            else:
                print(f"La tabla de {n} solo tiene {len(lineas)} líneas.")
    except FileNotFoundError:
        print(f"El archivo 'tabla-{n}.txt' no existe.")


def main():
    while True:
        print("\n----- Menú -----")
        print("1. Crear tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Mostrar línea específica de la tabla")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            n = int(input("Introduce un número entre 1 y 10 para la tabla: "))
            if 1 <= n <= 10:
                crear_tabla_multiplicar(n)
            else:
                print("El número debe estar entre 1 y 10.")

        elif opcion == '2':
            n = int(input("Introduce un número entre 1 y 10 para leer la tabla: "))
            if 1 <= n <= 10:
                leer_tabla_multiplicar(n)
            else:
                print("El número debe estar entre 1 y 10.")

        elif opcion == '3':
            n = int(input("Introduce un número entre 1 y 10 para la tabla: "))
            m = int(input("Introduce la línea que quieres ver (1-10): "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                mostrar_linea_tabla(n, m)
            else:
                print("Los números deben estar entre 1 y 10.")

        elif opcion == '4':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Elige una opción del 1 al 4.")


if __name__ == "__main__":
    main()
