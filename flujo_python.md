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

---

## 💡 Recordatorio Rápido

**Git Ignora**, **venv Aísla**, **requirements.txt Replica**, y **pip Instala**.