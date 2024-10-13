def contar_lineas_codigo(ruta_archivo):
    """Cuenta las líneas de código, ignorando comentarios y líneas en blanco."""
    try:
        with open(ruta_archivo, "r") as archivo:
            lineas = archivo.readlines() 
            contador = 0  
            
            for linea in lineas:
                linea = linea.strip()  
                
                if linea and not linea.startswith('#'):
                    contador += 1
            
            return contador  
    except FileNotFoundError:
        print("El archivo no se encontró, verifica la ruta.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    ruta_archivo = input("Introduce la ruta del archivo .py: ")
    
    if not ruta_archivo.endswith('.py'):
        print("Por favor, ingresa un archivo que termine en .py.")
        return

    loc = contar_lineas_codigo(ruta_archivo)
    
    if loc is not None:
        print(f"Número de líneas de código en '{ruta_archivo}': {loc}")


if __name__ == "__main__":
    main()

