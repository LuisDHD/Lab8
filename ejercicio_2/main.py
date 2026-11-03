from datos import PRODUCTOS
from operaciones import generar_reporte

# Líneas descomentadas para mostrar los resultados de los datos base
print(generar_reporte(PRODUCTOS))
print(generar_reporte([]))

# Ejemplo adicional con print y su resultado esperado en un comentario
PRODUCTOS_EXTRA = [
    {"nombre": "jugo", "precio": 4, "stock": 10, "categoria": "bebida"},
    {"nombre": "empanada", "precio": 3, "stock": 0, "categoria": "comida"}
]
print(generar_reporte(PRODUCTOS_EXTRA))
# Resultado esperado:
# {'disponibles': ['jugo'], 'valor_total': 40, 'hay_agotados': True, 'categorias': {'comida', 'bebida'}, 'precios_con_recargo': [('jugo', 4.4)]}