# Reabastecimiento de inventario

Solución en Python del problema 3 del Banco de problemas de la Fase 5 de Fundamentos de Programación.

## ¿Qué hace el programa?

Revisa los artículos de una matriz de inventario. Compara el stock actual con el stock mínimo requerido y calcula cuántas unidades se deben pedir. Si el stock actual ya alcanza el mínimo, muestra que se deben pedir 0 unidades.

## Datos de cada artículo

Cada fila de la matriz contiene los datos en este orden:

```text
[código, nombre, stock actual, stock mínimo requerido]
```

## Cómo ejecutarlo

1. Asegúrate de tener Python instalado.
2. Abre una terminal en la carpeta donde está `reabastecimiento.py`.
3. Ejecuta:

```powershell
py reabastecimiento.py
```

## Resultado esperado

El programa muestra la cantidad por pedir para cada artículo:

| Artículo | Cantidad por pedir |
|---|---:|
| Cuadernos | 8 |
| Lápices | 0 |
| Borradores | 6 |
| Reglas | 0 |
| Marcadores | 12 |

## Archivos

- `reabastecimiento.py`: código fuente del programa.
