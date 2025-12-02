import pandas as pd

# ============================================================================
# GUÍA COMPLETA DE pd.merge() - TODOS LOS CASOS POSIBLES
# ============================================================================
# El método merge() fusiona dos DataFrames basándose en columnas comunes.
# Es equivalente a las operaciones JOIN en SQL.
# ============================================================================

print("=" * 80)
print("DATAFRAMES DE EJEMPLO PARA TODAS LAS DEMOSTRACIONES")
print("=" * 80)

# --- CREAMOS DOS DATAFRAMES SENCILLOS PARA LOS EJEMPLOS ---

# DataFrame de Empleados (izquierdo)
empleados = pd.DataFrame({
    'empleado_id': [1, 2, 3, 4],
    'nombre': ['Ana', 'Carlos', 'Diana', 'Eduardo'],
    'departamento_id': [10, 20, 10, 30]
})

print("\n--- DataFrame 1: EMPLEADOS ---")
print(empleados)
# Resultado:
#    empleado_id   nombre  departamento_id
# 0            1      Ana               10
# 1            2   Carlos               20
# 2            3    Diana               10
# 3            4  Eduardo               30

# DataFrame de Departamentos (derecho)
departamentos = pd.DataFrame({
    'departamento_id': [10, 20, 40],
    'nombre_dept': ['Ventas', 'IT', 'Marketing'],
    'ubicacion': ['Madrid', 'Barcelona', 'Valencia']
})

print("\n--- DataFrame 2: DEPARTAMENTOS ---")
print(departamentos)
# Resultado:
#    departamento_id nombre_dept  ubicacion
# 0               10      Ventas     Madrid
# 1               20          IT  Barcelona
# 2               40   Marketing   Valencia

print("\n" + "=" * 80)
print("OBSERVACIONES IMPORTANTES ANTES DE EMPEZAR:")
print("=" * 80)
print("- Eduardo (empleado_id=4) está en departamento_id=30 (que NO existe en departamentos)")
print("- Departamento 40 (Marketing) NO tiene ningún empleado")
print("- Esto nos permitirá ver cómo se comportan los diferentes tipos de merge")
print()


# ============================================================================
# 1. INNER JOIN (how='inner') - INTERSECCIÓN
# ============================================================================
print("\n" + "=" * 80)
print("1. INNER JOIN - Solo filas que coinciden en AMBOS DataFrames")
print("=" * 80)
print("Sintaxis: df1.merge(df2, on='columna_comun', how='inner')")
print("Resultado: Solo empleados que tienen un departamento que existe")
print()

inner = empleados.merge(departamentos, on='departamento_id', how='inner')
print(inner)
# Resultado esperado:
#    empleado_id nombre  departamento_id nombre_dept  ubicacion
# 0            1    Ana               10      Ventas     Madrid
# 1            2 Carlos               20          IT  Barcelona
# 2            3  Diana               10      Ventas     Madrid
#
# NOTA: Eduardo (dept 30) y Marketing (dept 40) NO aparecen porque no hay coincidencia

print("\n¿Por qué 3 filas? Ana y Diana están en dept 10, Carlos en dept 20.")
print("Eduardo NO aparece porque su dept 30 no existe en 'departamentos'.")
print("Marketing NO aparece porque no tiene empleados.")


# ============================================================================
# 2. LEFT JOIN (how='left') - TODAS LAS FILAS DE LA IZQUIERDA
# ============================================================================
print("\n" + "=" * 80)
print("2. LEFT JOIN - Todas las filas del DataFrame IZQUIERDO (empleados)")
print("=" * 80)
print("Sintaxis: df1.merge(df2, on='columna_comun', how='left')")
print("Resultado: TODOS los empleados, con info del dept si existe (o NaN si no)")
print()

left = empleados.merge(departamentos, on='departamento_id', how='left')
print(left)
# Resultado esperado:
#    empleado_id   nombre  departamento_id nombre_dept  ubicacion
# 0            1      Ana               10      Ventas     Madrid
# 1            2   Carlos               20          IT  Barcelona
# 2            3    Diana               10      Ventas     Madrid
# 3            4  Eduardo               30         NaN        NaN
#
# NOTA: Eduardo aparece pero con NaN en nombre_dept y ubicacion (dept 30 no existe)

print("\n¿Por qué 4 filas? Mantiene TODOS los empleados.")
print("Eduardo aparece con NaN porque su departamento_id=30 no existe en 'departamentos'.")


# ============================================================================
# 3. RIGHT JOIN (how='right') - TODAS LAS FILAS DE LA DERECHA
# ============================================================================
print("\n" + "=" * 80)
print("3. RIGHT JOIN - Todas las filas del DataFrame DERECHO (departamentos)")
print("=" * 80)
print("Sintaxis: df1.merge(df2, on='columna_comun', how='right')")
print("Resultado: TODOS los departamentos, con empleados si existen (o NaN si no)")
print()

right = empleados.merge(departamentos, on='departamento_id', how='right')
print(right)
# Resultado esperado:
#    empleado_id nombre  departamento_id nombre_dept  ubicacion
# 0          1.0    Ana               10      Ventas     Madrid
# 1          3.0  Diana               10      Ventas     Madrid
# 2          2.0 Carlos               20          IT  Barcelona
# 3          NaN    NaN               40   Marketing   Valencia
#
# NOTA: Marketing aparece pero sin empleados (NaN en empleado_id y nombre)

print("\n¿Por qué 4 filas? Mantiene TODOS los departamentos.")
print("Marketing aparece con NaN en empleado_id y nombre (no tiene empleados).")
print("Eduardo NO aparece (su dept 30 no está en la tabla de departamentos).")


# ============================================================================
# 4. OUTER JOIN (how='outer') - TODAS LAS FILAS DE AMBOS
# ============================================================================
print("\n" + "=" * 80)
print("4. OUTER JOIN (FULL JOIN) - Todas las filas de AMBOS DataFrames")
print("=" * 80)
print("Sintaxis: df1.merge(df2, on='columna_comun', how='outer')")
print("Resultado: TODOS los empleados Y TODOS los departamentos (NaN donde no coincida)")
print()

outer = empleados.merge(departamentos, on='departamento_id', how='outer')
print(outer)
# Resultado esperado:
#    empleado_id   nombre  departamento_id nombre_dept  ubicacion
# 0          1.0      Ana               10      Ventas     Madrid
# 1          2.0   Carlos               20          IT  Barcelona
# 2          3.0    Diana               10      Ventas     Madrid
# 3          4.0  Eduardo               30         NaN        NaN
# 4          NaN      NaN               40   Marketing   Valencia
#
# NOTA: Eduardo (dept sin info) Y Marketing (dept sin empleados) ambos aparecen

print("\n¿Por qué 5 filas? Combina TODOS los datos de ambas tablas.")
print("Eduardo: empleado sin departamento válido (NaN en datos de dept).")
print("Marketing: departamento sin empleados (NaN en datos de empleados).")


# ============================================================================
# 5. MERGE CON COLUMNAS DE DIFERENTES NOMBRES
# ============================================================================
print("\n" + "=" * 80)
print("5. MERGE cuando las columnas tienen NOMBRES DIFERENTES")
print("=" * 80)

# Creamos un nuevo DataFrame donde la columna se llama diferente
empleados_v2 = pd.DataFrame({
    'empleado_id': [1, 2, 3],
    'nombre': ['Ana', 'Carlos', 'Diana'],
    'dept_id': [10, 20, 10]  # <-- Nota: se llama 'dept_id' en lugar de 'departamento_id'
})

print("\n--- Empleados v2 (con columna 'dept_id') ---")
print(empleados_v2)

print("\nUsamos left_on y right_on para especificar las columnas:")
print("Sintaxis: df1.merge(df2, left_on='col_izq', right_on='col_der', how='inner')")
print()

merge_diff_names = empleados_v2.merge(
    departamentos, 
    left_on='dept_id',           # Columna en empleados_v2
    right_on='departamento_id',  # Columna en departamentos
    how='inner'
)

print(merge_diff_names)
# Resultado:
#    empleado_id nombre  dept_id  departamento_id nombre_dept  ubicacion
# 0            1    Ana       10               10      Ventas     Madrid
# 1            2 Carlos       20               20          IT  Barcelona
# 2            3  Diana       10               10      Ventas     Madrid
#
# NOTA: Aparecen AMBAS columnas (dept_id Y departamento_id) con los mismos valores

print("\nNOTA: Cuando usas left_on/right_on, ambas columnas aparecen en el resultado.")


# ============================================================================
# 6. MERGE POR MÚLTIPLES COLUMNAS
# ============================================================================
print("\n" + "=" * 80)
print("6. MERGE por MÚLTIPLES COLUMNAS a la vez")
print("=" * 80)

# Creamos DataFrames donde necesitamos coincidir en MÁS de una columna
ventas = pd.DataFrame({
    'producto': ['Laptop', 'Mouse', 'Laptop', 'Teclado'],
    'tienda': ['Madrid', 'Madrid', 'Barcelona', 'Madrid'],
    'cantidad': [5, 20, 3, 15]
})

precios = pd.DataFrame({
    'producto': ['Laptop', 'Mouse', 'Laptop', 'Monitor'],
    'tienda': ['Madrid', 'Madrid', 'Barcelona', 'Madrid'],
    'precio': [800, 15, 850, 200]
})

print("\n--- Ventas ---")
print(ventas)

print("\n--- Precios ---")
print(precios)

print("\nMerge por ['producto', 'tienda'] simultáneamente:")
print("Sintaxis: df1.merge(df2, on=['col1', 'col2'], how='inner')")
print()

merge_multiple = ventas.merge(precios, on=['producto', 'tienda'], how='inner')
print(merge_multiple)
# Resultado:
#   producto    tienda  cantidad  precio
# 0   Laptop    Madrid         5     800
# 1    Mouse    Madrid        20      15
# 2   Laptop Barcelona         3     850
#
# NOTA: Laptop en Madrid y Laptop en Barcelona se tratan como diferentes
# Teclado no aparece (no tiene precio), Monitor no aparece (no tiene ventas)

print("\nSolo coincide si AMBAS columnas (producto Y tienda) son iguales.")


# ============================================================================
# 7. MERGE CON SUFIJOS PARA COLUMNAS DUPLICADAS
# ============================================================================
print("\n" + "=" * 80)
print("7. MERGE con SUFIJOS cuando hay columnas con el mismo nombre")
print("=" * 80)

# Ambos DataFrames tienen una columna 'nombre'
personas_ciudad = pd.DataFrame({
    'id': [1, 2, 3],
    'nombre': ['Ana', 'Carlos', 'Diana'],
    'ciudad_id': [100, 200, 100]
})

ciudades = pd.DataFrame({
    'ciudad_id': [100, 200],
    'nombre': ['Madrid', 'Barcelona'],  # <-- Misma columna 'nombre'
    'pais': ['España', 'España']
})

print("\n--- Personas ---")
print(personas_ciudad)

print("\n--- Ciudades ---")
print(ciudades)

print("\nSin sufijos (genera nombres automáticos _x y _y):")
merge_auto = personas_ciudad.merge(ciudades, on='ciudad_id', how='inner')
print(merge_auto)
# Las columnas 'nombre' se convierten en 'nombre_x' y 'nombre_y'

print("\n\nCon sufijos personalizados usando suffixes=('_persona', '_ciudad'):")
merge_custom = personas_ciudad.merge(
    ciudades, 
    on='ciudad_id', 
    how='inner',
    suffixes=('_persona', '_ciudad')
)
print(merge_custom)
# Ahora las columnas son 'nombre_persona' y 'nombre_ciudad'


# ============================================================================
# 8. MERGE CON INDICADOR
# ============================================================================
print("\n" + "=" * 80)
print("8. MERGE con INDICADOR para saber el origen de cada fila")
print("=" * 80)
print("El parámetro indicator=True añade una columna '_merge' que indica:")
print("  - 'left_only': solo existe en el DataFrame izquierdo")
print("  - 'right_only': solo existe en el DataFrame derecho")
print("  - 'both': existe en ambos DataFrames")
print()

merge_indicator = empleados.merge(
    departamentos, 
    on='departamento_id', 
    how='outer',
    indicator=True
)

print(merge_indicator)
# La columna '_merge' muestra el origen de cada fila

print("\n\nFiltrar solo filas que vienen del DataFrame izquierdo:")
solo_izquierda = merge_indicator[merge_indicator['_merge'] == 'left_only']
print(solo_izquierda)
# Eduardo (dept 30) solo está en empleados

print("\n\nFiltrar solo filas que vienen del DataFrame derecho:")
solo_derecha = merge_indicator[merge_indicator['_merge'] == 'right_only']
print(solo_derecha)
# Marketing (dept 40) solo está en departamentos


# ============================================================================
# 9. MERGE CON ÍNDICES EN LUGAR DE COLUMNAS
# ============================================================================
print("\n" + "=" * 80)
print("9. MERGE usando ÍNDICES en lugar de columnas")
print("=" * 80)

# DataFrames con índices significativos
clientes = pd.DataFrame({
    'nombre': ['Juan', 'María', 'Pedro'],
    'ciudad': ['Madrid', 'Barcelona', 'Sevilla']
}, index=[101, 102, 103])  # índice = cliente_id

pedidos = pd.DataFrame({
    'producto': ['Laptop', 'Mouse', 'Monitor'],
    'precio': [800, 15, 200]
}, index=[101, 102, 104])  # índice = cliente_id

print("\n--- Clientes (índice = cliente_id) ---")
print(clientes)

print("\n--- Pedidos (índice = cliente_id) ---")
print(pedidos)

print("\nMerge usando left_index=True y right_index=True:")
merge_index = clientes.merge(
    pedidos, 
    left_index=True, 
    right_index=True, 
    how='inner'
)
print(merge_index)
# Solo clientes 101 y 102 tienen pedidos

print("\n\nOtra forma: pd.merge con on solo funciona con columnas,")
print("pero puedes convertir el índice en columna con .reset_index()")


# ============================================================================
# RESUMEN VISUAL DE LOS TIPOS DE JOIN
# ============================================================================
print("\n" + "=" * 80)
print("RESUMEN VISUAL - ¿Cuál usar?")
print("=" * 80)

print("""
┌─────────────────────────────────────────────────────────────────────────┐
│ TIPO DE JOIN │ FILAS RESULTANTES                                        │
├──────────────┼──────────────────────────────────────────────────────────┤
│ INNER        │ Solo las que coinciden en AMBOS DataFrames               │
│              │ Caso de uso: Solo quiero datos completos                 │
│              │                                                           │
│ LEFT         │ TODAS del izquierdo, completando con NaN si no coinciden │
│              │ Caso de uso: Quiero todos los empleados, tengan o no     │
│              │              departamento válido                          │
│              │                                                           │
│ RIGHT        │ TODAS del derecho, completando con NaN si no coinciden   │
│              │ Caso de uso: Quiero todos los departamentos, tengan o no │
│              │              empleados                                    │
│              │                                                           │
│ OUTER        │ TODAS de ambos, completando con NaN donde falte          │
│              │ Caso de uso: Análisis completo, ver qué falta en cada    │
│              │              tabla                                        │
└──────────────┴──────────────────────────────────────────────────────────┘

PARÁMETROS IMPORTANTES:
  - on='columna'           → Cuando ambas tienen el mismo nombre
  - left_on / right_on     → Cuando las columnas tienen nombres diferentes
  - on=['col1', 'col2']    → Para hacer merge por múltiples columnas
  - how='inner|left|right|outer' → Tipo de join
  - suffixes=('_x', '_y')  → Para columnas duplicadas
  - indicator=True         → Añade columna '_merge' con el origen
  - left_index / right_index → Para merge por índices
""")

print("\n" + "=" * 80)
print("FIN DE LA GUÍA COMPLETA DE pd.merge()")
print("=" * 80)
