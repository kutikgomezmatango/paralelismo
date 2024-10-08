import multiprocessing
import time

# Función que busca la letra 'ñ' en una parte de la cadena, con retraso de 1 segundo por iteración
def buscar_letra(cadena, inicio, fin, resultado, proceso_id):
    inicio_proceso = time.time()  # Inicio del cronómetro para el proceso
    for i in range(inicio, fin):
        time.sleep(1)  # Simula un retraso de 1 segundo en cada iteración
        if cadena[i] == 'ñ':
            resultado[proceso_id] = i  # Almacena la posición encontrada
            print(f"Encontrado por proceso {proceso_id} en posición {i}")
            break  # Terminar el proceso si encuentra la letra
    tiempo_total = time.time() - inicio_proceso
    return tiempo_total  # Retornar el tiempo que tomó el proceso

# Función principal para controlar el número de procesos
def ejecutar_busqueda(cadena, num_procesos):
    longitud_cadena = len(cadena)
    tamaño_bloque = longitud_cadena // num_procesos
    procesos = []
    resultado = multiprocessing.Manager().list([-1] * num_procesos)  # Lista compartida entre procesos

    inicio_total = time.time()  # Inicio del cronómetro total

    # Crear los procesos
    for i in range(num_procesos):
        inicio_bloque = i * tamaño_bloque
        if i == num_procesos - 1:
            fin_bloque = longitud_cadena  # El último proceso toma el resto
        else:
            fin_bloque = inicio_bloque + tamaño_bloque
        
        proceso = multiprocessing.Process(target=buscar_letra, args=(cadena, inicio_bloque, fin_bloque, resultado, i))
        procesos.append(proceso)
        proceso.start()

    # Esperar a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()

    # Verificar si se encontró la letra 'ñ'
    for posicion in resultado:
        if posicion != -1:
            print(f"La letra 'ñ' fue encontrada en la posición: {posicion}")
            break
    else:
        print("La letra 'ñ' no fue encontrada en la cadena.")
    
    print(f"Tiempo total: {time.time() - inicio_total:.6f} segundos")

# Ejecución del código
if __name__ == "__main__":
    cadena = "asdhhashdjkasdhkjahñ"
    num_procesos = int(input("Introduce el número de procesos (1-8): "))
    ejecutar_busqueda(cadena, num_procesos)
