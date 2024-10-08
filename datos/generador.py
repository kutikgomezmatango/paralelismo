import random

# Función para generar una secuencia de ADN aleatoria de tamaño N
def generar_adn_gato(longitud):
    bases = ['A', 'C', 'T', 'G']
    return ''.join(random.choice(bases) for _ in range(longitud))

# Generar y guardar la secuencia de ADN en un archivo
def guardar_adn_archivo(nombre_archivo, longitud):
    adn = generar_adn_gato(longitud)
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(adn)
    print(f"Secuencia de ADN guardada en {nombre_archivo}")

# Generar un archivo con ADN de un gato simulado
if __name__ == "__main__":
    nombre_archivo = "datos/adn_gato.txt"  # Ruta en la carpeta 'datos'
    longitud_adn = 10000  # Longitud de la secuencia de ADN
    guardar_adn_archivo(nombre_archivo, longitud_adn)
