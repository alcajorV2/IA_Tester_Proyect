# Alcajor 07/09/2024
#
# Description:
#   - This code can be used to test if the logic of a code has changed with respect to its update. 
#   - This can be very useful for developers to make sure that they have not made any mistakes in 
#   optimizing the code with respect to the original.

from faker import Faker
import time
import json
import importlib.util
from tqdm import tqdm
import signal
import sys

# Generación de datos JSON con Faker
fake = Faker()

def generar_datos_json(n):
    datos = []
    for _ in range(n):
        item = {
            "nombre": fake.name(),
            "edad": fake.random_int(min=18, max=80),
            "direccion": fake.address(),
            "email": fake.email()
        }
        datos.append(item)
    return datos

# Función para cargar módulos desde archivos
def cargar_modulo_desde_archivo(ruta_archivo, nombre_modulo):
    spec = importlib.util.spec_from_file_location(nombre_modulo, ruta_archivo)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

# Cargar los módulos
modulo_no_optimizado = cargar_modulo_desde_archivo(r'C:\...\codigo_no_optimizado.py', 'codigo_no_optimizado') #Introduzir path del fichero original.
modulo_optimizado = cargar_modulo_desde_archivo(r'C:\...\codigo_optimizado.py', 'codigo_optimizado') #Introducir path del fichero nuevo.

# Comparación de Resultados
def comparar_resultados(resultados_original, resultados_optimizado):
    return resultados_original == resultados_optimizado

# Generar datos de entrada
datos_entrada = generar_datos_json(1000)

# Manejo de la señal SIGINT (Ctrl + C)
def signal_handler(sig, frame):
    print("\nInterrupción recibida. Cerrando el programa...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Comparar resultados con barra de progreso
for i in tqdm(range(len(datos_entrada)), desc="Comparando resultados..."):
    resultado_original = modulo_no_optimizado.procesar_datos_no_optimizado([datos_entrada[i]])
    resultado_optimizado = modulo_optimizado.procesar_datos_optimizado([datos_entrada[i]])
    time.sleep(0.0001)
    
    if not comparar_resultados(resultado_original, resultado_optimizado):
        print("\nLa lógica ha cambiado en el siguiente caso:")
        print("Entrada:", datos_entrada[i])
        print("Resultado Original:", resultado_original)
        print("Resultado Optimizado:", resultado_optimizado)
        break
else:
    print("\nLa lógica no ha cambiado.")
