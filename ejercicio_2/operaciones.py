from functools import reduce

def generar_reporte(productos):
    # Lambda para calcular el recargo del 10% redondeado a dos decimales
    aplicar_recargo = lambda precio: round(precio * 1.10, 2)
    
    return {
        "disponibles": list(map(lambda p: p["nombre"], filter(lambda p: p["stock"] > 0, productos))),
        
        "valor_total": reduce(lambda acc, val: acc + val, map(lambda p: p["precio"] * p["stock"], productos), 0),
        
        "hay_agotados": any(map(lambda p: p["stock"] == 0, productos)),
        
        "categorias": {p["categoria"] for p in productos},
        
        "precios_con_recargo": [(p["nombre"], aplicar_recargo(p["precio"])) for p in productos if p["stock"] > 0]
    }