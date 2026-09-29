from blog.modelos import Autor, Post, Blog
from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu
from blog.validaciones import validar_post


def mostrar_resultados(resultados):

    if not resultados:
        print("No se encontraron posts.")
        return

    for post in resultados:
        print(
            "-",
            post.titulo,
            "| Autor:",
            post.autor.nombre
        )


def crear_post(blog):

    print("\n--- CREAR NUEVO POST ---")

    titulo = input("Título: ").strip()
    contenido = input("Contenido: ").strip()
    autor_nombre = input("Autor: ").strip()
    tags_texto = input("Tags separados por coma: ").strip()

    estado = input(
        "Estado (borrador/publicado/archivado): "
    ).strip().lower()

    if (
        titulo == ""
        or contenido == ""
        or autor_nombre == ""
        or tags_texto == ""
        or estado == ""
    ):
        print("Error: ningún campo puede estar vacío.")
        return

    autor = Autor(
        autor_nombre,
        "Autor del blog"
    )

    tags = []

    for tag in tags_texto.split(","):
        tags.append(tag.strip())

    if blog.posts:
        nuevo_id = max(post.id for post in blog.posts) + 1
    else:
        nuevo_id = 1

    nuevo_post = Post(
        nuevo_id,
        titulo,
        contenido,
        autor,
        tags,
        estado
    )

    valido, mensaje = validar_post(nuevo_post)

    if valido:
        blog.agregar_post(nuevo_post)
        print("Post creado correctamente.")

    else:
        print("No se pudo crear el post:", mensaje)


if __name__ == "__main__":

    posts_cargados = cargar_posts()

    blog = Blog(posts_cargados)

    while True:

        opcion = mostrar_menu()

        if opcion == 1:

            blog.listar_posts()

        elif opcion == 2:

            termino = input(
                "Buscar por titulo: "
            ).strip()

            resultados = blog.buscar_por_titulo(
                termino
            )

            mostrar_resultados(resultados)

        elif opcion == 3:

            tag = input(
                "Escribí un tag: "
            ).strip()

            resultados = blog.filtrar_por_tag(
                tag
            )

            mostrar_resultados(resultados)

        elif opcion == 4:

            crear_post(blog)

        elif opcion == 5:

            print("\nValidación de posts:")

            for post in blog.posts:

                valido, mensaje = validar_post(post)

                if valido:
                    print(
                        "Post",
                        post.id,
                        ": válido"
                    )

                else:
                    print(
                        "Post",
                        post.id,
                        ": error -",
                        mensaje
                    )

        elif opcion == 6:

            guardar_posts(
                blog.obtener_posts()
            )

        elif opcion == 7:

            print(
                "Gracias por usar el sistema del blog. ¡Hasta luego!"
            )
            break

        elif opcion is not None:

            print("Opción inválida, intenta de nuevo.")