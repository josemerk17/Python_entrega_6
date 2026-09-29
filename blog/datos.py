import json
from pathlib import Path

from blog.modelos import Post


ARCHIVO_POSTS = Path(__file__).resolve().parent.parent / "posts.json"


def cargar_posts():

    try:
        with open(ARCHIVO_POSTS, "r", encoding="utf-8") as archivo:

            datos = json.load(archivo)

            posts = []

            for dato in datos:
                post = Post.desde_diccionario(dato)
                posts.append(post)

            return posts

    except FileNotFoundError:
        print("No existe posts.json. Se iniciará sin posts.")
        return []

    except json.JSONDecodeError:
        print("El archivo posts.json está vacío o contiene datos inválidos.")
        return []

    except Exception as error:
        print("Error al cargar los posts:", error)
        return []


def guardar_posts(posts):

    try:

        datos = []

        for post in posts:
            datos.append(post.a_diccionario())

        with open(ARCHIVO_POSTS, "w", encoding="utf-8") as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print("Posts guardados correctamente.")

    except Exception as error:
        print("Error al guardar los posts:", error)
