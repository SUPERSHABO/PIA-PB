def best(productos):
    productos_validos = [producto for producto in productos if producto.get("rating") is not None]
    if productos_validos:
        mejor_producto = max(productos_validos, key=lambda x: x.get("rating"))
        nombre = mejor_producto.get("name")
        calificacion = mejor_producto.get("rating")
        precio = mejor_producto.get("price")
        return nombre, calificacion, precio
    else:
        return None

def worst(productos):
    productos_validos = [producto for producto in productos if producto.get("rating") is not None]
    if productos_validos:
        peor_producto = min(productos_validos, key=lambda x: x.get("rating"))
        nombre = peor_producto.get("name")
        calificacion = peor_producto.get("rating")
        precio = peor_producto.get("price")
        return nombre, calificacion, precio
    else:
        return None