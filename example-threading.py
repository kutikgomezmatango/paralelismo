import threading
import time

# Función para simular una tarea con multihilos
def funcion_1(inicio, fin):
    for i in range(inicio, fin):
        time.sleep(1)  # Simula un retraso de 1 segundo en cada iteración
    print(f"Terminado por hilo: {threading.current_thread().name}")

# Función principal para controlar el número de hilos
def ejecutar_con_hilos(num_hilos):
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista base
    tamaño_bloque = len(lista) // num_hilos  # Dividimos la lista en bloques por número de hilos
    hilos = []

    inicio = time.time()  # Inicio del cronómetro

    # Crear los hilos
    for i in range(num_hilos):
        inicio_bloque = i * tamaño_bloque
        if i == num_hilos - 1:
            fin_bloque = len(lista)  # El último hilo toma el resto
        else:
            fin_bloque = inicio_bloque + tamaño_bloque
        
        hilo = threading.Thread(target=funcion_1, args=(inicio_bloque, fin_bloque))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    print(f"Tiempo total: {time.time() - inicio} segundos")

# Ejecutar con el número de hilos deseado
if __name__ == "__main__":
    num_hilos = int(input("Introduce el número de hilos (1-8): "))
    ejecutar_con_hilos(num_hilos)
