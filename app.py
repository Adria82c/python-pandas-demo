# ETL Básico con Pandas: Extracción, Transformación y Carga de Datos
import pandas as pd
import numpy as np

# --- 1. EXTRACT (Creación o Extracción de datos) ---
print("\n--- 1. Extracción (Creación del DataFrame) ---")

# Simulamos datos crudos
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Edad': [25, 30, 35, 40, 22],
    'Salario_Bruto': [50000, 65000, 75000, np.nan, 48000], # np.nan simula un valor faltante
    'Departamento': ['Ventas', 'IT', 'Ventas', 'Marketing', 'IT']
}

df = pd.DataFrame(data)
print("\nDataFrame Original:")
print(df)
print("-" * 30)

# --- 2. TRANSFORM (Limpieza y Modificación de datos) ---
print("--- 2. Transformación ---")

# a) Limpieza: Rellenar valores faltantes (imputación)
# Rellenamos el salario faltante (np.nan) con el promedio de la columna
salario_promedio = df['Salario_Bruto'].mean()
df['Salario_Bruto'].fillna(salario_promedio, inplace=True)

# b) Creación de una nueva columna: Calcular Salario Neto (simulación simple)
# Asumimos una retención fija del 30%
df['Salario_Neto'] = df['Salario_Bruto'] * 0.70

# c) Filtrado: Seleccionar solo empleados de 'IT'
df_it = df[df['Departamento'] == 'IT']

print("\nDataFrame Transformado (Solo IT, Salario Neto calculado):")
print(df_it)
print("-" * 30)

# --- 3. LOAD (Carga de datos) ---
print("--- 3. Carga ---")

# Cargamos el DataFrame transformado a un nuevo archivo CSV
output_filename = 'empleados_it_transformados.csv'
df_it.to_csv(output_filename, index=False)

print(f"\nDatos cargados exitosamente en: {output_filename}")
print("-" * 30)

# Verificamos que el archivo se haya creado (opcional)
import os
print(f"Verificando si el archivo existe: {os.path.exists(output_filename)}")