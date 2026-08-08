# 🚀 FastAPI - To-Do List Web App

Aplicación web ligera, moderna y funcional para la gestión de tareas pendientes. Desarrollada como proyecto de aprendizaje utilizando el framework **FastAPI**, renderizado de plantillas con **Jinja2** y diseño responsive con **Bootstrap 5**.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

---

## 🛠️ Características

- **Diseño limpio y moderno:** Interfaz responsiva utilizando Bootstrap 5 e iconos de FontAwesome.
- **Renderizado del lado del servidor:** Uso de Jinja2 para la integración fluida entre Python y HTML.
- **Endpoints asíncronos:** Arquitectura backend optimizada con FastAPI y Uvicorn.
- **Documentación automática:** Acceso a Swagger UI generado automáticamente en `/docs`.

---

## 💻 Stack Tecnológico

| Categoría | Tecnología |
| :--- | :--- |
| **Backend** | Python 3, FastAPI, Starlette |
| **Frontend** | HTML5, Jinja2, Bootstrap 5, FontAwesome |
| **Servidor ASGI** | Uvicorn |
| **Manejo de Formularios** | `python-multipart` |

---

## 📂 Estructura del Proyecto

```text
fastapi-todo-app/
├── templates/
│   └── index.html      # Plantilla principal con Bootstrap 5
├── main.py             # Código del servidor y rutas de FastAPI
├── requirements.txt    # Lista de dependencias del proyecto
└── .gitignore          # Archivos excluidos de Git
```
⚡ Instalación y Ejecución Local

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

    Clonar el repositorio:
    Bash

    git clone [https://github.com/AngelLisandro2024/fastapi-todo-app.git](https://github.com/AngelLisandro2024/fastapi-todo-app.git)
    cd fastapi-todo-app

    Crear y activar entorno virtual:
    Bash

    python3 -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate

    Instalar dependencias:
    Bash

    pip install -r requirements.txt

    Iniciar el servidor local:
    Bash

    uvicorn main:app --reload

    Abrir en el navegador:

        Aplicación Web: http://127.0.0.1:8000

        Documentación Interactiva (Swagger UI): http://127.0.0.1:8000/docs

👨‍💻 Autor

Diseñado y desarrollado por Ángel Fernández (@AngelLisandro2024).
