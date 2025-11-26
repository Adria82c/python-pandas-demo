# 🐍 Resumen: Flujo de Trabajo y Portabilidad en Python

Este documento resume los procesos y comandos esenciales para mantener un entorno de desarrollo Python (VS Code, Intérprete, Proyectos) completamente portable en una unidad USB, haciendo hincapié en el aislamiento de proyectos (venv).

## 1. Configuración del Intérprete Portable (VS Code)

El primer paso es decirle a tu instalación portable de VS Code dónde encontrar el ejecutable de Python. Esto asegura que el intérprete esté disponible en todos tus proyectos.

**Método: settings.json (Global)**

**Acción:** Añadir configuración del intérprete
   **Ubicación:** Archivo `settings.json` de VS Code Portable (dentro de la carpeta data)
   **Comando:** `"python.defaultInterpreterPath": "E:\\Software\\python314\\python.exe"`
   **Propósito:** Configura el intérprete por defecto para todos los proyectos. Sin esto, VS Code no sabe dónde está python.exe

## 2. Aislamiento de Proyectos con venv

Un **Entorno Virtual (venv)** es una copia aislada y ligera del intérprete de Python, dedicada exclusivamente a un solo proyecto. Es la clave de la portabilidad y la replicabilidad.

### 2.1. Concepto y Justificación (El Porqué)

**Aislamiento**
   **Descripción:** Copia ligera del intérprete dedicada a un proyecto
   **Beneficio:** Previene conflictos entre versiones de librerías

**Replicabilidad**
   **Descripción:** Documenta dependencias en `requirements.txt`
   **Beneficio:** Permite recrear el entorno en cualquier equipo

**Peso y Limpieza**
   **Descripción:** Librerías se guardan en carpeta del proyecto
   **Beneficio:** Mantiene limpia la instalación base de Python

**¿Por qué NO usar venv?**
- ❌ Todas las librerías se mezclan en el intérprete portable
- ❌ Conflictos entre proyectos (Proyecto A: requests==1.0 vs Proyecto B: requests==3.0)
- ❌ Imposible recrear el entorno exacto en otra máquina

### 2.2. Flujo de Comandos (Creación y Activación)

Estos comandos se ejecutan en la terminal del proyecto (Git Bash en tu caso).

**Paso 1: Crear venv**
   **Comando:** `python -m venv .venv`
   **Resultado:** Crea la carpeta `.venv` en tu proyecto

**Paso 2: Activar venv**
   **Comando:** `source .venv/Scripts/activate`
   **Resultado:** Aparece `(.venv)` en el terminal

> **⚠️ Importante en Windows:** Se usa `Scripts` en lugar de `bin` (típico de Linux/Mac)

## 3. Manejo de Dependencias (pip y Flujo ETL)

Una vez que el venv está activo, todas las instalaciones de librerías se aíslan.

### 3.1. Instalación de Librerías

> **Regla de oro:** `pip install` se ejecuta en la **terminal** (después de activar venv), **NUNCA** dentro del código Python.

**En Terminal (con venv activo)**
   **Acción:** Instalar librería
   **Comando:** `pip install pandas`

**En Archivo Python (.py)**
   **Acción:** Importar librería
   **Código:** `import pandas as pd`

### 3.2. Proceso de Reproducibilidad (El Flujo Portable)

Para garantizar la replicabilidad en cualquier equipo, debes subir el `requirements.txt` a Git y forzar la recreación del entorno en el equipo de destino.

#### **Generar y Subir Dependencias (PC Original):**

Asegúrate de que la carpeta `.venv` esté en `.gitignore` (es pesada y dependiente del sistema operativo).

```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "feat: añadir requisitos de librerías"
git push
```

#### **Recuperación en PC Nuevo (Flujo Obligatorio):**

Al clonar el repositorio, el venv y las librerías **DEBEN** recrearse e instalarse.

```bash
# 1. CLONAR y NAVEGAR
git clone [url-del-repositorio]
cd [nombre-del-proyecto]

# 2. RECREAR EL VENV
python -m venv .venv

# 3. ACTIVAR EL VENV
source .venv/Scripts/activate

# 4. INSTALAR DEPENDENCIAS
pip install -r requirements.txt
```



### 3.3. El Compromiso con el Espacio (Peso)

La carpeta `.venv` es pesada (100-200 MB por librerías como Pandas).

**Estrategia para ahorrar espacio:**

**Antes de cerrar proyecto**
   **Acción:** Generar requirements
   **Comando:** `pip freeze > requirements.txt`

**Liberar espacio en USB**
   **Acción:** Eliminar venv
   **Comando:** `rm -rf .venv`

**Volver a trabajar**
   **Acción:** Recrear entorno
   **Referencia:** Ver flujo en sección 3.2

> **💾 Tip:** El `requirements.txt` es pequeño (pocos KB) pero contiene toda la información para recrear el entorno completo.

## 4. Empaquetado y Distribución (PyInstaller)

PyInstaller convierte tu script de Python y todas sus dependencias (incluyendo el intérprete de Python) en un ejecutable autónomo (.exe).

### 4.1. Concepto de Aplicación Autónoma

**Resultado**
   **Detalle:** Un archivo .exe para Windows
   **Característica:** Ejecutable independiente y autónomo

**Requisito en Destino**
   **Detalle:** NO necesita que el usuario final tenga Python, pip, o las librerías (Pandas, NumPy, etc.) instaladas
   **Característica:** Completamente portable

**Proceso**
   **Detalle:** PyInstaller empaqueta una versión mínima del intérprete de Python, tu código y todas las dependencias en un solo paquete binario
   **Característica:** Empaquetado automático e inteligente

### 4.2. Opciones de Empaquetado

**Modo Múltiples Archivos (Por defecto)**
   **Comando:** `pyinstaller tu_app.py`
   **Resultado:** Crea una carpeta (`dist/tu_app`) con el ejecutable (`tu_app.exe`) y todas las DLLs, librerías y recursos auxiliares necesarios
   **Distribución:** La carpeta completa debe distribuirse

**Modo OneFile (Recomendado para distribución simple)**
   **Comando:** `pyinstaller --onefile tu_app.py`
   **Resultado:** Crea un solo archivo `tu_app.exe`. Al ejecutarse, este .exe se descomprime temporalmente en la memoria o en una carpeta oculta de archivos temporales de Windows
   **Distribución:** Solo se distribuye el .exe

### 4.3. Reempaquetado con Configuración

**Reempaquetar (Método Recomendado)**
   **Paso 1:** Borrar carpetas previas
   **Comando:** `rm -rf build dist`
   **Propósito:** Limpia compilaciones anteriores para evitar conflictos

   **Paso 2:** Reempaquetar con configuración
   **Comando:** `pyinstaller tu_app.spec`
   **Resultado:** Utiliza el archivo de configuración `.spec` generado en la primera ejecución
   **Ventaja:** Mantiene configuraciones personalizadas y optimizaciones específicas


---

## 💡 Recordatorio Rápido

**Git Ignora**, **venv Aísla**, **requirements.txt Replica**, **pip Instala**, y **pyinstaller Empaqueta**.