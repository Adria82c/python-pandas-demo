# pip install pandas openpyxl numpy

import pandas as pd
import numpy as np

# --- 1. EXTRACT (Creación o Extracción de datos) ---
print("\n--- 1. Extracción (Creación del DataFrame) ---")
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'María'],
    'Edad': [25, 30, 35, 40, 22, 28],
    # Incluimos un carácter especial ('ñ') para confirmar la correcta codificación
    'Salario_Bruto': [50000, 65000, 75000, np.nan, 48000, 60000], 
    'Departamento': ['Ventas', 'IT', 'Ventas', 'Marketing', 'IT', 'Recursos Humanos']
}

df = pd.DataFrame(data)
# ... (El código de Extracción y Transformación permanece igual) ...

# --- 2. TRANSFORM (Limpieza y Modificación de datos) ---
print("--- 2. Transformación ---")

# a) Limpieza: Rellenar valores faltantes (imputación)
salario_promedio = df['Salario_Bruto'].mean()
df['Salario_Bruto'].fillna(salario_promedio, inplace=True)

# b) Creación de una nueva columna: Calcular Salario Neto
df['Salario_Neto'] = df['Salario_Bruto'] * 0.70

# c) Filtrado: Seleccionar solo empleados de 'IT'
df_it = df[df['Departamento'] == 'IT']

print("\nDataFrame Transformado (Solo IT, Salario Neto calculado):")
print(df_it)
print("-" * 30)

# --- 3. LOAD (Carga de datos a XLSX) ---
print("--- 3. Carga ---")

# Nuevo nombre de archivo con extensión XLSX
output_filename = 'empleados_it_transformados.xlsx'

# Usamos df_it.to_excel()
# index=False evita escribir la columna de índices de Pandas en el archivo.
# Excel maneja UTF-8 de forma nativa.
try:
    df_it.to_excel(output_filename, index=False, engine='openpyxl')
    print(f"\nDatos cargados exitosamente en el archivo XLSX: {output_filename}")
except ImportError:
    print("\nERROR: La librería 'openpyxl' no está instalada.")
    print("Por favor, instálala usando: pip install openpyxl")
except Exception as e:
    print(f"\nOcurrió un error al escribir el archivo XLSX: {e}")

print("-" * 30)