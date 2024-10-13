import requests
import zipfile

# URL de la imagen
url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Paso 1: Descargar la imagen
response = requests.get(url)
if response.status_code == 200:
    with open("imagen_descargada.jpg", "wb") as f:
        f.write(response.content)
    print("Imagen descargada con éxito.")
else:
    print("Error al descargar la imagen.")

# Paso 2: Crear un archivo ZIP
zip_filename = "imagen_zip.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write("imagen_descargada.jpg")
print(f"Archivo zip '{zip_filename}' creado con éxito.")

# Paso 3: Descomprimir el archivo ZIP
with zipfile.ZipFile(zip_filename, 'r') as zipf:
    zipf.extractall("imagen_extraida")
print("Archivo zip descomprimido con éxito.")
