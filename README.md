# API de Gestión de Usuarios con FastAPI

Este proyecto es una API de gestión de usuarios implementada con FastAPI. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre usuarios en una base de datos. La API está diseñada para ser rápida, eficiente y fácil de usar, aprovechando las ventajas de FastAPI, como la generación de documentación interactiva y la validación de datos.

## Comenzando

Sigue estas instrucciones para obtener una copia del proyecto ejecutándose en tu máquina local para propósitos de desarrollo y prueba.

### Prerrequisitos

Necesitarás tener Docker instalado en tu máquina. Si no lo tienes, sigue las instrucciones para instalar Docker en tu sistema operativo aquí: [Instalar Docker](https://docs.docker.com/get-docker/).

### Instalación

Para instalar y ejecutar la API en tu entorno local, sigue estos pasos:

1. Clona el repositorio en tu máquina local:
git clone https://github.com/devecode/crud-fastAPI.git

2. Navega al directorio del proyecto:
3. Construye y ejecuta el contenedor Docker usando `docker-compose`:
docker-compose up -d --build

Esto construirá la imagen Docker de tu aplicación (si no se ha construido antes) y luego iniciará el contenedor. 

4. Una vez que el contenedor está ejecutando, la API estará accesible en [http://localhost:8000](http://localhost:8000).

### Uso

Para comenzar a usar la API, puedes navegar a [http://localhost:8000/docs](http://localhost:8000/docs) en tu navegador web para acceder a la documentación interactiva de Swagger UI, donde podrás realizar peticiones directamente desde la interfaz.

### Desarrollo

Si deseas contribuir al proyecto o realizar modificaciones, aquí están los pasos recomendados para el desarrollo:

1. Asegúrate de tener todas las dependencias instaladas utilizando el entorno Docker.
2. Realiza tus cambios en el código fuente.
3. Para probar tus cambios localmente, utiliza `docker-compose up` para reconstruir y reiniciar los contenedores.

## Construido Con

* [FastAPI](https://fastapi.tiangolo.com/) - El framework web usado.
* [Docker](https://www.docker.com/) - Manejador de contenedores.
* [MongoDB Atlas](https://cloud.mongodb.com//) - Manejador de base de datos NoSql.


