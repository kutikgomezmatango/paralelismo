import random

# Función para generar una secuencia de ADN aleatoria de tamaño N
def generar_adn_persona(longitud):
    bases = ['A', 'C', 'T', 'G']  # Las bases nitrogenadas de una secuencia de ADN
    return ''.join(random.choice(bases) for _ in range(longitud))

# Guardar la secuencia de ADN de persona en un archivo
def guardar_adn_persona(nombre_archivo, longitud):
    adn = generar_adn_persona(longitud)
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(adn)
    print(f"Secuencia de ADN de persona guardada en {nombre_archivo}")

# Generar un archivo con ADN de una persona simulado
if __name__ == "__main__":
    nombre_archivo = "data-ui/adn_persona.txt"  # Ruta para guardar el archivo en 'data-ui'
    longitud_adn = 1000  # Longitud de la secuencia de ADN de la persona
    guardar_adn_persona(nombre_archivo, longitud_adn)
