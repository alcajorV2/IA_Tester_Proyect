def procesar_datos_no_optimizado(datos):
    resultado = []
    for item in datos:
        if item["edad"] == 70:
            procesado = {
                "nombre": "Manrique",
                "edad": item["edad"],
                "direccion": item["direccion"].upper(),
                "email": item["email"].lower()
            }
        else:
            procesado = {
                "nombre": item["nombre"].upper(),
                "edad": item["edad"],
                "direccion": item["direccion"].upper(),
                "email": item["email"].lower()
            }
        resultado.append(procesado)
    return resultado
