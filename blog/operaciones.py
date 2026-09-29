# Operaciones principales del blog


def listar_posts(lista):

    print("\nPosts disponibles:")

    for post in lista:

        titulo = post.get("titulo", "Sin título")
        autor = post.get("autor", {})
        estado = post.get("estado", "Sin estado")

        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre", "Autor desconocido")
        else:
            nombre_autor = "Autor desconocido"

        print(
            "-",
            titulo,
            "| Autor:",
            nombre_autor,
            "| Estado:",
            estado
        )


def buscar_por_titulo(lista, termino):

    if termino == "":
        print("La búsqueda no puede estar vacía.")
        return

    encontrado = False

    for post in lista:

        titulo = post.get("titulo", "")

        if termino.lower() in titulo.lower():
            print("-", titulo)
            encontrado = True

    if encontrado == False:
        print("No se encontraron posts con ese titulo.")


def filtrar_por_tag(lista, tag_buscado):

    if tag_buscado == "":
        print("El tag no puede estar vacío.")
        return

    encontrado = False

    for post in lista:

        tags = post.get("tags", [])

        if isinstance(tags, list):

            for tag in tags:

                if tag_buscado.lower() == tag.lower():
                    print("-", post.get("titulo", "Sin título"))
                    encontrado = True
                    break

    if encontrado == False:
        print("No se encontraron posts con ese tag.")