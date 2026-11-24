"""Calcula cuánto debe pedirse para completar el stock mínimo de cada artículo."""


def calcular_cantidad_pedido(stock_actual, stock_minimo):
    """Devuelve las unidades necesarias para alcanzar el stock mínimo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


# Cada fila tiene este orden:
# [código del artículo, nombre, stock actual, stock mínimo requerido]
inventario = [
    ["A101", "Cuadernos", 12, 20],
    ["A102", "Lápices", 35, 30],
    ["A103", "Borradores", 4, 10],
    ["A104", "Reglas", 8, 8],
    ["A105", "Marcadores", 3, 15],
]

print("INFORME DE REABASTECIMIENTO")
print("Artículo                Cantidad por pedir")
print("-" * 43)

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedido = calcular_cantidad_pedido(stock_actual, stock_minimo)
    print(f"{nombre:<23} {cantidad_pedido:>5}")
