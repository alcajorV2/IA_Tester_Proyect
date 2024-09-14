def procesar_datos_optimizado(datos):
    return [
        {
            "nombre": item["nombre"].upper(),
            "edad": item["edad"],
            "direccion": item["direccion"].upper(),
            "email": item["email"].lower()
        }
        for item in datos
    ]
