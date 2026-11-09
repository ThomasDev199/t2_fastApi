# TechGear

**TechGear** es una plataforma de comercio electrónico orientada a la venta de productos tecnológicos. El proyecto integra un frontend desarrollado con Django y una API REST construida con FastAPI, utilizando MongoDB Atlas como base de datos.

## Enlaces del proyecto

- **Frontend:** https://t2-fast-api.vercel.app/
- **Repositorio en GitHub:** https://github.com/ThomasDev199/t2_fastApi
- **API Backend:** https://t2-fastapi-2.onrender.com/

## Tecnologías utilizadas

### Frontend
- Python
- Django
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- FastAPI
- MongoDB Atlas
- JWT (JSON Web Tokens)

### Despliegue
- Vercel para el frontend.
- Render para la API.
- GitHub para el control de versiones.

## Funcionalidades principales

- Registro e inicio de sesión de usuarios.
- Autenticación mediante JWT.
- Gestión de usuarios con roles de cliente y administrador.
- Visualización del catálogo de productos.
- Consulta de información y disponibilidad de productos.
- Creación y consulta de pedidos.
- Descuento de inventario al realizar pedidos.
- Panel administrativo para la gestión de productos.
- Integración entre Django y FastAPI.

## Estructura del proyecto

```text
t2_fastApi/
│
├── techgear_api/
│   ├── app/
│   │   └── main.py
│   └── requirements.txt
│
├── techgear_web/
│   ├── store/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── requirements.txt
│
├── manage.py
├── requirements.txt
└── README.md
```

## Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/ThomasDev199/t2_fastApi.git
```

### 2. Entrar al proyecto

```bash
cd t2_fastApi
```

### 3. Crear un entorno virtual

```bash
python -m venv venv
```

### 4. Activar el entorno virtual

En Windows:

```powershell
.\venv\Scripts\Activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Configurar variables de entorno

Configurar las siguientes variables según el entorno:

```env
SECRET_KEY=tu_clave_secreta
API_URL=http://127.0.0.1:8000
```

También se debe configurar la conexión a MongoDB Atlas en el backend.

### 7. Ejecutar el frontend

```bash
python manage.py runserver 8001
```

El frontend estará disponible en:

```text
http://127.0.0.1:8001/
```

### 8. Ejecutar el backend

Desde la carpeta `techgear_api`:

```bash
uvicorn app.main:app --reload --port 8000
```

La API estará disponible en:

```text
http://127.0.0.1:8000/
```

## Arquitectura del sistema

TechGear utiliza una arquitectura separada en dos componentes:

- **Django:** administra la interfaz web, las plantillas y la interacción con los usuarios.
- **FastAPI:** proporciona los endpoints REST para autenticación, usuarios, productos y pedidos.
- **MongoDB Atlas:** almacena la información del sistema.

Django consume los servicios de FastAPI mediante solicitudes HTTP.

## Autenticación y seguridad

- Autenticación mediante tokens JWT.
- Gestión de roles de usuario.
- Variables de entorno para configuraciones sensibles.
- Conexión a base de datos mediante MongoDB Atlas.

No se deben subir claves secretas, contraseñas ni credenciales al repositorio.

## Autor

**Thomas Cano Zapata**

Proyecto desarrollado como iniciativa de aprendizaje y aplicación de conocimientos en desarrollo de software.

---

**TechGear – Tecnología, innovación y soluciones digitales.**
