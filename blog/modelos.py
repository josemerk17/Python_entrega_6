# Clases principales del sistema


class Autor:

    def __init__(self, nombre, bio, especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales or []

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos.get("nombre", "Autor desconocido"),
            datos.get("bio", ""),
            datos.get("especialidad", ""),
            datos.get("redes_sociales", [])
        )


class Post:

    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def a_diccionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.a_diccionario(),
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def desde_diccionario(cls, datos):
        autor = Autor.desde_diccionario(
            datos.get("autor", {})
        )

        return cls(
            datos.get("id"),
            datos.get("titulo", ""),
            datos.get("contenido", ""),
            autor,
            datos.get("tags", []),
            datos.get("estado", "borrador")
        )


class Blog:

    def __init__(self, posts=None):
        self.posts = posts or []

    def listar_posts(self):

        if not self.posts:
            print("No hay posts disponibles.")
            return

        print("\nPosts disponibles:")

        for post in self.posts:
            print(
                "-",
                post.titulo,
                "| Autor:",
                post.autor.nombre,
                "| Estado:",
                post.estado
            )

    def buscar_por_titulo(self, termino):

        resultados = []

        for post in self.posts:
            if termino.lower() in post.titulo.lower():
                resultados.append(post)

        return resultados

    def filtrar_por_tag(self, tag_buscado):

        resultados = []

        for post in self.posts:

            for tag in post.tags:

                if tag_buscado.lower() == tag.lower():
                    resultados.append(post)
                    break

        return resultados

    def agregar_post(self, post):
        self.posts.append(post)

    def obtener_posts(self):
        return self.posts