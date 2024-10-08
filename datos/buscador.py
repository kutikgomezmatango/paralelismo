# Función para leer el archivo de ADN y cargarlo en memoria
def leer_adn_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        adn = archivo.read()
    return adn

# Función para buscar una subsecuencia que no coincida en el ADN
def buscar_no_coincidencia(adn, patron):
    if patron not in adn:
        print(f"El patrón '{patron}' no fue encontrado en la secuencia de ADN.")
    else:
        print(f"El patrón '{patron}' fue encontrado en la secuencia de ADN.")

# Ejecución del código para buscar una no coincidencia
if __name__ == "__main__":
    nombre_archivo = "datos/adn_gato.txt"  # Ruta del archivo en la carpeta 'datos'
    
    # Leer la secuencia de ADN desde el archivo
    secuencia_adn = leer_adn_archivo(nombre_archivo)
    
    # Definir un patrón que probablemente no esté en la secuencia
    patron = "GGCCCG"  # Un patrón raro que probablemente no esté en el ADN
    
    # Buscar la no coincidencia en la secuencia de ADN
    buscar_no_coincidencia(secuencia_adn, patron)
