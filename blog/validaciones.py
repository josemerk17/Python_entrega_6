def validar_post(post):

    if post.titulo.strip() == "":
        return False, "el título está vacío"

    if post.contenido.strip() == "":
        return False, "el contenido está vacío"

    if post.autor.nombre.strip() == "":
        return False, "el autor no tiene nombre"

    if not isinstance(post.tags, list):
        return False, "los tags deben ser una lista"

    estados_validos = (
        "borrador",
        "publicado",
        "archivado"
    )

    if post.estado not in estados_validos:
        return False, "el estado no es válido"

    return True, "válido"