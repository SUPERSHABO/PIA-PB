def calcular_precio_promedio(productos):
    precios = [float(producto['price']) for producto in productos 
               if producto['price'] is not None]
    promedio = sum(precios) / len(precios)
    return round(promedio, 2) 

def obtener_producto_mas_caro(productos):
    productos_validos = [producto for producto in productos 
                         if producto['price'] is not None]
    mas_caro = max(productos_validos, key=lambda x: float(x['price']))
    return mas_caro['name'], mas_caro['price']

def obtener_producto_mas_barato(productos):
    productos_validos = [producto for producto in productos 
                         if producto['price'] is not None and float(producto['price']) > 0]
    mas_barato = min(productos_validos, key=lambda x: float(x['price']))
    return mas_barato['name'], mas_barato['price']