# FastAPI + PostgreSQL + Docker

Este proyecto es una plantilla básica para crear una API RESTful con **FastAPI** y una base de datos **PostgreSQL** utilizando **Docker** y **SQLAlchemy** para la gestión de datos.

Incluye:
- Un contenedor para la aplicación FastAPI.
- Un contenedor para la base de datos PostgreSQL.
- Un script de inicialización de la base de datos con una tabla `users` y datos de ejemplo.

---

## Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL 15](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## ¿Qué pretende este mini proyecto?

Este proyecto tiene como objetivo servir como base para desarrollos más complejos en FastAPI con una base de datos relacional. Es ideal para comprender y poner en práctica conceptos fundamentales de desarrollo backend moderno con contenedores.

### Objetivos principales:

- **Sentar las bases para una instalación desde Docker** de una API construida con FastAPI, conectada a una base de datos PostgreSQL.
- **Probar el correcto funcionamiento del entorno**: desde la construcción de imágenes y ejecución de contenedores hasta la conexión y persistencia de datos en la base de datos.
- **Visualizar y entender las configuraciones necesarias** en los distintos ficheros clave:
  - `docker-compose.yml`: definición y coordinación de los servicios (API y base de datos).
  - `init.py`: creación de tablas e inserción de datos iniciales mediante SQLAlchemy.
  - `requirements.txt`: declaración de dependencias del entorno Python.
- **Disponer de un punto de partida reutilizable** para futuros desarrollos con autenticación, endpoints personalizados, migraciones y más.
