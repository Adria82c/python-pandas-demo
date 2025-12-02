import pandas as pd # Importa la librería Pandas, esencial para la manipulación de datos.
from typing import final # Importa 'final' para definir constantes inmutables.

# --- 1. CARGA Y EXPLORACIÓN DEL DATASET ---

# URL conocida para cargar un archivo CSV del Titanic. Tipamos la variable como 'final str' para indicar que es una constante.
TITANIC_URL: final[str] = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'

# pd.read_csv()
# Lee el dataset directamente desde la URL de Internet y lo guarda en el DataFrame 'df'.
df = pd.read_csv(TITANIC_URL)

# df.head()
# Muestra las primeras 5 filas del DataFrame por defecto.
print("--- df.head() - Primeras 5 filas del DataFrame original ---")
print(df.head())
# Resultado esperado (Primeras dos líneas, aproximado):
# -------------------------------------------------------------
# | PassengerId | Survived | Pclass | Name | Sex | Age | SibSp | Parch | Ticket | Fare | Cabin | Embarked |
# | 1           | 0        | 3      | Braund, Mr. Owen Harris | male | 22.0 | 1 | 0 | A/5 21171 | 7.25 | NaN | S |
# | 2           | 1        | 1      | Cumings, Mrs. John Bradley | female | 38.0 | 1 | 0 | PC 17599 | 71.2833 | C85 | C |
# -------------------------------------------------------------

# df.tail()
# Muestra las últimas 5 filas del DataFrame.
print("\n--- df.tail() - Últimas 5 filas ---")
print(df.tail(2)) # Mostramos solo las 2 últimas para brevedad.

# df.sample()
# Devuelve una muestra aleatoria del DataFrame.
print("\n--- df.sample(n=1) - Muestra aleatoria ---")
print(df.sample(n=1)) # Muestra una fila aleatoria.

# df.columns
# Muestra el nombre de todas las columnas.
print("\n--- df.columns - Nombres de columnas ---")
print(df.columns)

# df.index
# Muestra el objeto índice del DataFrame (en este caso, un RangeIndex).
print("\n--- df.index - Información del índice ---")
print(df.index)

# df.info()
# Muestra un resumen del DataFrame: tipos de datos, valores no nulos y uso de memoria.
print("\n--- df.info() - Resumen informativo ---")
df.info()

# df.describe()
# Genera estadísticas descriptivas para columnas numéricas.
print("\n--- df.describe() - Estadísticas descriptivas ---")
print(df.describe())

# df.shape y len(df)
# Muestra las dimensiones (filas, columnas) y el número de filas.
print(f"\nDimensiones (filas, columnas) con .shape: {df.shape}")
print(f"Número de filas con len(df): {len(df)}")


# --- 2. SELECCIÓN DE DATOS (INDEXING) ---

# Selección de un subconjunto de columnas (Lista entre corchetes)
df_subconjunto = df[['Name', 'Age', 'Fare']].copy() # Usamos .copy() para evitar SettingWithCopyWarning
print("\n--- Selección de columnas ['Name', 'Age', 'Fare'] ---")
print(df_subconjunto.head(2)) # Mostramos solo las primeras 2 filas para brevedad.

# df.select_dtypes()
# Selecciona solo las columnas que son de tipo flotante (float64).
df_floats = df.select_dtypes(include='float64')
print("\n--- df.select_dtypes(include='float64') - Columnas flotantes ---")
print(df_floats.head(2))

# df.iloc
# Accede a las filas y columnas por su posición numérica (índice 0 y 1, columna 3 y 4).
# Aquí selecciona las 2 primeras filas y las columnas 'Name' (3) y 'Sex' (4).
print("\n--- df.iloc[0:2, 3:5] - Selección por posición ---")
print(df.iloc[0:2, 3:5])

# df.loc
# Accede a las filas y columnas por su etiqueta (índice 0 y 1, columnas 'Name' y 'Sex').
print("\n--- df.loc[0:1, ['Name', 'Sex']] - Selección por etiqueta ---")
print(df.loc[0:1, ['Name', 'Sex']])


# --- 3. FILTRADO BOLEANO Y CONSULTAS ---

# Filtrado Booleano
# Crea un DataFrame con solo mujeres de la Primera Clase (Pclass=1).
mujeres_primera = df[(df['Sex'] == 'female') & (df['Pclass'] == 1)]
print("\n--- Filtrado Booleano (Mujeres en 1ra Clase) ---")
print(mujeres_primera.head(2))

# El operador ~ (tilde)
# Filtra a todos los pasajeros que NO embarcaron en 'S' (Southampton).
no_southampton = df[~(df['Embarked'] == 'S')]
print(f"\nNúmero de filas de pasajeros NO embarcados en S: {len(no_southampton)}")

# df.query()
# Filtra las mismas filas anteriores, pero usando una sintaxis de string.
query_result = df.query('Sex == "male" and Age > 60')
print("\n--- df.query('Sex == \"male\" and Age > 60') - Consulta por string ---")
print(query_result.head(2))


# --- 4. AGREGACIÓN Y RESUMEN DE DATOS ---

# Métodos de Agregación (.mean(), .sum(), etc.)
# Calcula el promedio de edad de todos los pasajeros.
media_edad = df['Age'].mean()
print(f"\nMedia de edad de pasajeros: {media_edad:.2f}")

# df.agg()
# Calcula múltiples agregaciones (mínimo y máximo) en la columna 'Fare'.
agg_fare = df.agg({'Fare': ['min', 'max']})
print("\n--- df.agg() - Múltiples agregaciones en 'Fare' ---")
print(agg_fare)

# df['col'].unique()
# Muestra los valores únicos en la columna 'Embarked' (puerto de embarque).
print("\n--- df['Embarked'].unique() - Valores únicos ---")
print(df['Embarked'].unique())

# df['col'].nunique()
# Cuenta cuántos valores únicos hay.
print(f"Número de puertos de embarque únicos: {df['Embarked'].nunique()}")

# df['col'].value_counts()
# Muestra el conteo de ocurrencias de cada valor en la columna 'Pclass'.
print("\n--- df['Pclass'].value_counts() - Conteo de valores ---")
print(df['Pclass'].value_counts())

# df.groupby() + Agregación
# Agrupa por sexo y calcula la media de la tarifa para cada grupo.
tarifa_por_sexo = df.groupby('Sex')['Fare'].mean().reset_index() # .reset_index() para convertir el índice en columna
print("\n--- df.groupby(['Sex'])['Fare'].mean() ---")
print(tarifa_por_sexo)


# df.reset_index()
# Convierte el índice (Sex) resultante del groupby en una columna normal.
print("\n--- .reset_index() (Resultado de Groupby) ---")
print(tarifa_por_sexo.head())


# --- 5. TRANSFORMACIÓN DE COLUMNAS AVANZADAS ---

# df.rank()
# Calcula el rango de la tarifa (el pasaje más barato tiene el rango más bajo).
df['Fare_Rank'] = df['Fare'].rank(method='min')
print("\n--- df['Fare_Rank'] con .rank() - Primeras 2 filas ---")
print(df[['Fare', 'Fare_Rank']].head(2))

# df.shift()
# Crea una columna con la tarifa de la fila anterior (desplazamiento de 1).
df['Prev_Fare'] = df['Fare'].shift(1)
print("\n--- df['Prev_Fare'] con .shift() - Primeras 2 filas ---")
print(df[['Fare', 'Prev_Fare']].head(2))

# df.cumsum()
# Calcula la suma acumulativa de la columna 'SibSp'.
df['SibSp_CumSum'] = df['SibSp'].cumsum()
print("\n--- df['SibSp_CumSum'] con .cumsum() - Primeras 2 filas ---")
print(df[['SibSp', 'SibSp_CumSum']].head(2))

# df.rolling()
# Calcula la media móvil de 3 períodos en la columna 'Fare' (útil para series de tiempo).
df['Fare_3_Rolling_Mean'] = df['Fare'].rolling(window=3).mean()
print("\n--- .rolling(window=3).mean() - Primeras 5 filas (para ver el cálculo) ---")
print(df[['Fare', 'Fare_3_Rolling_Mean']].head(5))

# df.clip()
# Limita los valores de la columna 'Age' a un rango entre 10 y 60 años.
df['Age_Clipped'] = df['Age'].clip(lower=10, upper=60)
print("\n--- df['Age_Clipped'] con .clip() - Valores limitados ---")
print(df[['Age', 'Age_Clipped']].head(2))


# --- 6. ASIGNACIÓN Y ORDENACIÓN ---

# Creación de nueva columna por asignación directa
# Crea una columna que indica si el pasajero tiene familia a bordo.
df['Has_Family'] = df['SibSp'] + df['Parch'] > 0
print("\n--- df['Has_Family'] - Primeras 2 filas ---")
print(df[['Has_Family']].head(2))

# df.assign()
# Crea otra columna, esta vez usando el método encadenable .assign().
df = df.assign(Is_Child = df['Age'] < 18)
print("\n--- df.assign(Is_Child) - Primeras 2 filas ---")
print(df[['Is_Child']].head(2))

# df.sort_values()
# Ordena el DataFrame por la columna 'Fare' de forma descendente.
df_sorted_fare = df.sort_values(by='Fare', ascending=False)
print("\n--- df.sort_values(by='Fare', ascending=False) - Pasajeros más caros ---")
print(df_sorted_fare[['Name', 'Fare']].head(2))

# df.sort_index()
# Ordena el DataFrame por su índice. (Usamos el original para demostrarlo).
df_sorted_index = df_sorted_fare.sort_index()
print("\n--- df.sort_index() - Pasajeros ordenados por índice original ---")
print(df_sorted_index[['Name', 'Fare']].head(2))


# --- 7. LIMPIEZA DE DATOS FALTANTES ---

# df.isna()
# Comprueba dónde hay valores faltantes (NaN) y los suma por columna.
print("\n--- df.isna().sum() - Conteo de valores faltantes ---")
print(df.isna().sum())

# df.fillna()
# Rellena los valores faltantes en 'Age' con el valor promedio de la columna.
age_mean = df['Age'].mean()
df['Age_Filled'] = df['Age'].fillna(age_mean)
print(f"\nFilas faltantes en 'Age_Filled' después de fillna: {df['Age_Filled'].isna().sum()}")

# df.dropna()
# Elimina las filas que tienen valores faltantes en la columna 'Cabin'.
df_no_cabin_na = df.dropna(subset=['Cabin'])
print(f"Filas restantes después de .dropna(subset=['Cabin']): {len(df_no_cabin_na)}")


# --- 8. COMBINACIÓN DE DATAFRAMES ---

# Creamos un segundo DataFrame para la combinación
df_extra = pd.DataFrame({
    'Survived': [0, 1, 0, 1],
    'Status': ['Lost', 'Saved', 'Lost', 'Saved'],
    'New_Col': [100, 200, 300, 400]
})

# pd.concat()
# Combina dos DataFrames verticalmente (añade filas).
# NOTA: Para este ejemplo, solo usamos 4 filas de df original.
df_concat = pd.concat([df.head(4), df_extra], axis=0, ignore_index=True)
print("\n--- pd.concat(axis=0) - Combinación vertical ---")
print(df_concat['Survived', 'Embarked', 'New_Col'].tail(4)) # Mostramos solo las últimas 4 filas para ver el efecto.

# df.merge()
# Fusiona dos DataFrames basándose en un valor de columna común ('Survived').
# Creamos un DF de mapeo para hacer el merge.
df_status = pd.DataFrame({
    'Survived': [0, 1],
    'Survival_Status': ['Perished', 'Rescued']
})
df_merged = df.merge(df_status, on='Survived', how='left') # left join
print("\n--- df.merge(on='Survived', how='left') - Fusión de datos ---")
print(df_merged[['Survived', 'Survival_Status']].head(2))


# --- 9. GUARDAR DATASET ---

# df.to_csv()
# Guarda el DataFrame modificado en un archivo CSV local, sin incluir el índice de Pandas.
# df.to_csv('titanic_modificado.csv', index=False)
# print("\nDataFrame guardado en 'titanic_modificado.csv'")

# df.to_excel()
# Guarda el DataFrame modificado en un archivo Excel local, sin incluir el índice de Pandas.
# df.to_excel('titanic_modificado.xlsx', index=False, engine='openpyxl')
# print("DataFrame guardado en 'titanic_modificado.xlsx'")