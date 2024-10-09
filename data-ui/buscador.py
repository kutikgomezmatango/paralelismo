import multiprocessing
import time

# Función para leer el archivo de ADN y cargarlo en memoria
def leer_adn_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            adn = archivo.read()
        return adn
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        return None

# Función que busca el patrón en una parte del ADN (usado por cada proceso)
def buscar_patron_parte(adn, patron, inicio, fin, resultado, proceso_id):
    posiciones = []
    for i in range(inicio, min(fin, len(adn)) - len(patron) + 1):
        if adn[i:i+len(patron)] == patron:
            posiciones.append(i)
    resultado[proceso_id] = posiciones  # Almacena las posiciones encontradas en el diccionario compartido

# Función principal para manejar la búsqueda utilizando múltiples procesos
def buscar_patron_multiprocesos(adn, patron, num_procesos):
    longitud_adn = len(adn)
    tamaño_bloque = longitud_adn // num_procesos  # Dividir el ADN en bloques para cada proceso
    resultado = multiprocessing.Manager().dict()  # Diccionario compartido para almacenar resultados
    procesos = []

    inicio_tiempo = time.time()  # Iniciar el cronómetro

    # Crear y asignar cada proceso para que busque en su parte del ADN
    for i in range(num_procesos):
        inicio_bloque = i * tamaño_bloque
        fin_bloque = (i + 1) * tamaño_bloque if i != num_procesos - 1 else longitud_adn
        proceso = multiprocessing.Process(target=buscar_patron_parte, args=(adn, patron, inicio_bloque, fin_bloque, resultado, i))
        procesos.append(proceso)
        proceso.start()

    # Esperar a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()

    # Combinar los resultados de todos los procesos
    posiciones_totales = []
    for pos_list in resultado.values():
        posiciones_totales.extend(pos_list)

    tiempo_total = time.time() - inicio_tiempo  # Calcular el tiempo total de búsqueda

    # Mostrar el resultado
    if posiciones_totales:
        print(f"El patrón '{patron}' fue encontrado en las posiciones: {sorted(posiciones_totales)}")
    else:
        print(f"El patrón '{patron}' no fue encontrado en la secuencia de ADN.")
    
    print(f"Tiempo total de búsqueda utilizando {num_procesos} procesos: {tiempo_total:.6f} segundos")

# Ejecución del código con multiprocesos
if __name__ == "__main__":
    nombre_archivo = "data-ui/adn_persona.txt"  # Ruta fija del archivo
    
    # Leer la secuencia de ADN desde el archivo
    secuencia_adn = leer_adn_archivo(nombre_archivo)
    
    if secuencia_adn:
        # Solicitar el patrón a buscar en la secuencia de ADN
        patron = input("Introduce el patrón de ADN que deseas buscar: ")
        
        # Solicitar el número de procesos (núcleos) que deseas utilizar
        num_procesos = int(input("Introduce el número de procesos (1-8): "))
        if num_procesos < 1 or num_procesos > 8:
            print("Por favor, introduce un número entre 1 y 8.")
        else:
            # Buscar el patrón utilizando multiprocesos
            buscar_patron_multiprocesos(secuencia_adn, patron, num_procesos)
