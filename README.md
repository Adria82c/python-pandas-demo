# ETL Básico con Pandas - Proyecto de Datos

Este proyecto implementa un proceso ETL (Extract, Transform, Load) básico utilizando Python y Pandas para procesar datos de empleados.

## 📋 Descripción del ETL

### 🔍 Extract (Extracción)
- **Fuente de datos**: Se crean datos simulados de empleados incluyendo:
  - Nombre
  - Edad
  - Salario Bruto
  - Departamento
- Los datos incluyen valores faltantes (`np.nan`) para simular datos del mundo real

### 🔄 Transform (Transformación)
El proceso de transformación incluye las siguientes operaciones:

1. **Limpieza de datos**:
   - Imputación de valores faltantes en `Salario_Bruto` usando el promedio de la columna

2. **Creación de nuevas columnas**:
   - Cálculo del `Salario_Neto` aplicando una retención del 30% sobre el salario bruto

3. **Filtrado de datos**:
   - Selección únicamente de empleados del departamento 'IT'

### 📤 Load (Carga)
- Los datos transformados se guardan en un archivo CSV: `empleados_it_transformados.csv`
- El archivo contiene únicamente los empleados del departamento IT con sus salarios netos calculados

## 🚀 Configuración del Entorno de Desarrollo

### 1. Crear y Activar el Entorno Virtual

#### En Windows (PowerShell/CMD):
```bash
# Crear el entorno virtual
python -m venv .venv

# Activar el entorno virtual
.venv\Scripts\activate
```

#### En Windows (Git Bash):
```bash
# Crear el entorno virtual
python -m venv .venv

# Activar el entorno virtual
source .venv/Scripts/activate
```

#### En macOS/Linux:
```bash
# Crear el entorno virtual
python3 -m venv .venv

# Activar el entorno virtual
source .venv/bin/activate
```

### 2. Instalación de Dependencias

Una vez activado el entorno virtual, instalar las dependencias:

```bash
# Instalar todas las dependencias desde requirements.txt
pip install -r requirements.txt
```

### 3. Verificar la Instalación

```bash
# Verificar que las dependencias se instalaron correctamente
pip list
```

Deberías ver las siguientes dependencias instaladas:
- `numpy==2.3.5`
- `pandas==2.3.3`
- `python-dateutil==2.9.0.post0`
- `pytz==2025.2`
- `six==1.17.0`
- `tzdata==2025.2`

## 📁 Estructura del Proyecto

```
py-project/
├── .venv/                          # Entorno virtual (generado)
├── app.py                          # Script principal del ETL
├── empleados_it_transformados.csv  # Archivo de salida (generado)
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Este archivo
```

## ▶️ Ejecución del Proyecto

1. **Asegúrate de que el entorno virtual esté activado**:
   ```bash
   # Windows (Git Bash)
   source .venv/Scripts/activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

2. **Ejecutar el script ETL**:
   ```bash
   python app.py
   ```

3. **Salida esperada**:
   - El script mostrará en consola los pasos del proceso ETL
   - Se generará el archivo `empleados_it_transformados.csv` con los datos procesados

## 📊 Datos de Salida

El archivo `empleados_it_transformados.csv` contendrá:
- Empleados únicamente del departamento 'IT'
- Valores de salario bruto sin valores faltantes
- Salario neto calculado (70% del salario bruto)

Ejemplo de salida:
```csv
Nombre,Edad,Salario_Bruto,Departamento,Salario_Neto
Bob,30,65000.0,IT,45500.0
Eva,22,48000.0,IT,33600.0
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Pandas**: Manipulación y análisis de datos
- **NumPy**: Operaciones numéricas y manejo de arrays

## 🔧 Comandos Útiles

### Desactivar el entorno virtual:
```bash
deactivate
```

### Actualizar requirements.txt (si añades nuevas dependencias):
```bash
pip freeze > requirements.txt
```

### Limpiar cache de pip:
```bash
pip cache purge
```

## 📝 Notas Adicionales

- Mantén siempre activado el entorno virtual cuando trabajes en el proyecto
- Si encuentras problemas con la instalación, verifica que tienes la versión correcta de Python
- El archivo `.venv/` no debe incluirse en el control de versiones (añádelo a `.gitignore`)

## 🤝 Contribuciones

Este es un proyecto educativo para aprender conceptos básicos de ETL con Python y Pandas.
