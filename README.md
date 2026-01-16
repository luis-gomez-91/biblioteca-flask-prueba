# Proyecto Flask CRUD - Sistema de Biblioteca

Sistema de gestión de biblioteca con Flask, SQLAlchemy, PostgreSQL y Bootstrap.

## 📋 Requisitos Previos

- Python 3.8 o superior
- PostgreSQL instalado y corriendo
- Git instalado
- pip (gestor de paquetes de Python)

## 📦 Instalación de Dependencias

Crea y activa un entorno virtual:

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

Instala las dependencias necesarias:

```bash
pip install Flask==3.0.0
pip install Flask-SQLAlchemy==3.1.1
pip install psycopg2-binary==2.9.9
pip install Flask-Migrate==4.0.5
pip install python-dotenv==1.0.0
```

Para generar el archivo `requirements.txt` con las dependencias que ya tienes instaladas en tu entorno virtual, usa este comando:

```bash
# Genera el archivo requirements.txt
pip freeze > requirements.txt
```

O crea un archivo `requirements.txt` manualmente con el siguiente contenido:

txt

```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
psycopg2-binary==2.9.9
Flask-Migrate==4.0.5
python-dotenv==1.0.0
```

E instala todo con:

````bash
pip install -r requirements.txt
```

## 🗂️ Estructura del Proyecto
```
proyecto-flask-biblioteca/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── autor_routes.py
│   │   ├── categoria_routes.py
│   │   └── libro_routes.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── autores/
│       │   ├── index.html
│       │   ├── create.html
│       │   └── edit.html
│       ├── categorias/
│       │   ├── index.html
│       │   ├── create.html
│       │   └── edit.html
│       └── libros/
│           ├── index.html
│           ├── create.html
│           └── edit.html
│
├── migrations/
├── .env
├── .gitignore
├── config.py
├── run.py
├── requirements.txt
└── README.md
````

## ⚙️ Configuración

### 1. Configurar PostgreSQL

Crea una base de datos en PostgreSQL:

sql

```sql
CREATE DATABASE biblioteca_db;
```

### 2. Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

env

````env
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/biblioteca_db
SECRET_KEY=tu_clave_secreta_aqui
FLASK_APP=run.py
FLASK_ENV=development
```

**Importante:** Reemplaza `usuario` y `contraseña` con tus credenciales de PostgreSQL.

### 3. Crear archivo .gitignore

Crea un archivo `.gitignore`:
```
venv/
__pycache__/
*.pyc
.env
*.db
migrations/
.DS_Store
````

## 🚀 Inicialización de la Base de Datos

### 1. Inicializar Alembic

```bash
flask db init
```

### 2. Crear la primera migración

```bash
flask db migrate -m "Creación inicial de tablas"
```

### 3. Aplicar la migración

```bash
flask db upgrade
```

## ▶️ Ejecutar la Aplicación

```bash
python run.py
```

La aplicación estará disponible en: `http://127.0.0.1:5000`

## 📝 Versionamiento con Git

### 1. Inicializar repositorio Git

```bash
git init
```

### 2. Agregar archivos al staging

```bash
git add .
```

### 3. Realizar primer commit

```bash
git commit -m "Configuración inicial del proyecto Flask con CRUD completo"
```

### 4. Crear repositorio en GitHub

Ve a [GitHub](https://github.com) y crea un nuevo repositorio llamado `flask-biblioteca-crud`

### 5. Conectar con el repositorio remoto

```bash
git remote add origin https://github.com/tu-usuario/flask-biblioteca-crud.git
git branch -M main
git push -u origin main
```

## 📚 Comandos Git Útiles

```bash
# Ver estado de los archivos
git status

# Crear una nueva rama
git checkout -b feature/nueva-funcionalidad

# Cambiar entre ramas
git checkout main

# Ver historial de commits
git log --oneline

# Actualizar desde el repositorio remoto
git pull origin main

# Subir cambios
git add .
git commit -m "Descripción de los cambios"
git push origin main
```

## 🔄 Comandos de Migración Útiles

```bash
# Crear una nueva migración después de cambios en modelos
flask db migrate -m "Descripción del cambio"

# Aplicar migraciones pendientes
flask db upgrade

# Revertir última migración
flask db downgrade

# Ver historial de migraciones
flask db history

# Ver estado actual
flask db current
```