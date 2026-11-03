"""
Ejercicio 1: Mapa de puestos
"""

def crear_mapa(puestos):
    # Comprensión de diccionario: (fila, columna) -> estado
    return {(f, c): estado for f, fila in enumerate(puestos) for c, estado in enumerate(fila)}


def obtener_disponibles(puestos):
    # Comprensión de conjuntos (set): coordenadas donde el estado es 0
    return {(f, c) for f, fila in enumerate(puestos) for c, estado in enumerate(fila) if estado == 0}


if __name__ == "__main__":
    # Tablero original del ejemplo
    puestos = [[1, 0, 1], [0, 0, 1]]

    # 1. Llamadas y comprobaciones principales
    mapa = crear_mapa(puestos)
    disponibles = obtener_disponibles(puestos)

    print("Mapa completo:", mapa)
    print("Puestos disponibles:", disponibles)
    print("Estado de (1, 2):", mapa[(1, 2)])

    # 2. Caso de prueba propio
    puestos_propio = [
        [0, 1],
        [1, 0],
        [0, 0]
    ]

    mapa_propio = crear_mapa(puestos_propio)
    disponibles_propio = obtener_disponibles(puestos_propio)

    print("\n--- Caso Propio ---")
    print("Mapa propio:", mapa_propio)
    print("Disponibles esperado: {(0, 0), (1, 1), (2, 0), (2, 1)}")
    print("Disponibles obtenido:", disponibles_propio)
    print("Estado de (0, 1) en mapa propio:", mapa_propio[(0, 1)])

# ANALISIS
# 1. ¿Cuántas celdas se revisan al obtener los disponibles en el ejemplo?
#    Se revisan 6 celdas (2 filas x 3 columnas).
#
# 2. ¿Cuántas se revisan para f filas y c columnas?
#    Se revisan (f * c) celdas en total.
#
# 3. ¿Y para n filas y n columnas?
#    Se revisan n * n (n²) celdas en total (Complejidad temporal O(n²)).