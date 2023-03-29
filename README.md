# Wiki It Academy API

Esta API Restful fue creada con el objetivo de permitir a los alumnos de It Academy compartir recursos y conocimientos sobre diferentes temas, organizados en categorías y temas específicos.

(Disclaimer: esta Api es solo un divertimento como programador. La It Academy no me ha encargado que haga semejante cosa; es solo un reto que me he planteado yo)

## Tecnologías utilizadas

-   Python
-   Django
-   Django Rest Framework
-   Simple JWT
-   drf-spectacular

## Funcionalidades

La API cuenta con los siguientes endpoints:

-   `api/users/register`: Registro de usuarios.
-   `api/users/login`: Inicio de sesión con autenticación JWT.
-   `api/users/refresh`: Renovación de token JWT.
-   `api/users/admin`: Acceso a una vista protegida para los usuarios con permisos de administrador.
-   `api/wiki/categories/`: Listado y creación de categorías.
-   `api/wiki/categories/<int:category_id>/`: Consulta, actualización y eliminación de categorías específicas.
-   `api/wiki/temas/`: Listado y creación de temas.
-   `api/wiki/temas/<int:tema_id>/`: Consulta, actualización y eliminación de temas específicos.
-   `api/wiki/wikis/`: Listado y creación de wikis.
-   `api/wiki/wikis/<int:wiki_id>/`: Consulta, actualización y eliminación de wikis específicas.

## Autenticación

La API utiliza autenticación basada en tokens JWT (JSON Web Tokens), los cuales se obtienen al hacer una petición de inicio de sesión a `api/users/login`. Para acceder a los endpoints protegidos, es necesario incluir el token JWT en la cabecera de la petición, de la siguiente manera:

makefileCopy code

`Authorization: Bearer <token>`

El token puede ser renovado con la petición a `api/users/refresh`.

## Esquema

La API también cuenta con un esquema generado automáticamente por drf-spectacular, el cual se puede consultar en la ruta `api/schema/`. Adicionalmente, se han incluido dos vistas opcionales para visualizar el esquema:

-   `api/schema/swagger-ui/`: Interfaz web generada con Swagger UI.

  ![Documentación renderizada en Swagger](/images/swagger-ui.png)

-   `api/schema/redoc/`: Interfaz web generada con ReDoc.

  ![Documentación renderizada en ReDoc](/images/redoc.png)

## Pon en marcha el proyecto

1.  Clona el repositorio en tu ordenador:

    `git clone https://github.com/ivanlegranbizarro/ita-wiki-django.git`

2.  Crea un entorno virtual para el proyecto:

    `python -m venv myenv`

3.  Activa el entorno virtual:

    -   En Windows:

        `myenv\Scripts\activate`

    -   En Linux o macOS:

        `source myenv/bin/activate`

4.  Instala las dependencias del proyecto con pip:

    `pip install -r requirements.txt`

5.  Renombra el archivo `.env.example` a `.env` y configura las variables de entorno`. Por defecto puedes usar una base de datos sqlite.

6.  Ejecuta las migraciones:

    `python manage.py migrate`

7.  Crea un superusuario para acceder al panel de administración:

    `python manage.py createsuperuser`

8.  Ejecuta el servidor de desarrollo:

    `python manage.py runserver`

9.  Abre el navegador y accede a la dirección `http://localhost:8000/`. Verás la página principal de la API.

10.  Para acceder al panel de administración, ingresa a la dirección `http://localhost:8000/admin/` e ingresa las credenciales del superusuario creado en el paso 7.
