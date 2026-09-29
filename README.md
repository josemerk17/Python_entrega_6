# Sistema de Blog por Consola

Sistema de blog desarrollado en Python utilizando Programación Orientada a Objetos y persistencia mediante JSON.

## Clases principales

### Autor

Representa al autor de una publicación.

### Post

Representa una publicación del blog. Cada Post contiene una instancia de la clase Autor.

### Blog

Administra la lista de publicaciones y permite listar, buscar, filtrar y agregar posts.

## Persistencia JSON

El sistema utiliza el archivo `posts.json` para guardar las publicaciones.

Cuando inicia el programa, los datos del archivo JSON se cargan y se convierten en objetos de Python.

Antes de guardar los posts, los objetos se convierten nuevamente en diccionarios compatibles con JSON.

## Funcionalidades

El sistema permite:

- Ver todos los posts.
- Buscar posts por título.
- Filtrar posts por tag.
- Crear nuevos posts.
- Validar posts.
- Guardar posts en JSON.

## Ejecución

Desde la carpeta raíz del proyecto ejecutar:

python main.py

## Cambios respecto al módulo anterior

El sistema ahora utiliza Programación Orientada a Objetos mediante las clases Autor, Post y Blog.

También incorpora persistencia mediante JSON, permitiendo conservar las publicaciones entre diferentes ejecuciones del programa.