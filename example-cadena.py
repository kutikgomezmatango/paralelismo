import threading
import time

# Función que busca la letra 'ñ' en una parte de la cadena, con retraso de 1 segundo por iteración
def buscar_letra(cadena, inicio, fin, resultado, hilo_id, tiempos_hilos):
    inicio_hilo = time.time()  # Inicio del cronómetro para el hilo
    for i in range(inicio, fin):
        time.sleep(1)  # Simula un retraso de 1 segundo en cada iteración
        if cadena[i] == 'ñ':
            resultado[hilo_id] = i  # Almacena la posición encontrada
            print(f"Encontrado por hilo {hilo_id} en posición {i}")
            break  # Terminar el hilo si encuentra la letra
    tiempos_hilos[hilo_id] = time.time() - inicio_hilo  # Tiempo que tomó el hilo

# Función principal para controlar el número de hilos
def ejecutar_busqueda(cadena, num_hilos):
    longitud_cadena = len(cadena)
    tamaño_bloque = longitud_cadena // num_hilos
    hilos = []
    resultado = [-1] * num_hilos  # Lista para almacenar el resultado de cada hilo
    tiempos_hilos = [0] * num_hilos  # Lista para almacenar el tiempo de cada hilo

    inicio_total = time.time()  # Inicio del cronómetro total

    # Crear los hilos
    for i in range(num_hilos):
        inicio_bloque = i * tamaño_bloque
        if i == num_hilos - 1:
            fin_bloque = longitud_cadena  # El último hilo toma el resto
        else:
            fin_bloque = inicio_bloque + tamaño_bloque
        
        hilo = threading.Thread(target=buscar_letra, args=(cadena, inicio_bloque, fin_bloque, resultado, i, tiempos_hilos))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    # Verificar si se encontró la letra 'ñ'
    for posicion in resultado:
        if posicion != -1:
            print(f"La letra 'ñ' fue encontrada en la posición: {posicion}")
            break
    else:
        print("La letra 'ñ' no fue encontrada en la cadena.")
    
    # Mostrar el tiempo que tomó cada hilo
    for hilo_id, tiempo in enumerate(tiempos_hilos):
        print(f"Tiempo que tomó el hilo {hilo_id}: {tiempo:.2f} segundos")
    
    print(f"Tiempo total: {time.time() - inicio_total:.2f} segundos")

# Ejecución del código
if __name__ == "__main__":
    cadena = "asdhhashdjkasdhkjah"
    num_hilos = int(input("Introduce el número de hilos (1-8): "))
    ejecutar_busqueda(cadena, num_hilos)
