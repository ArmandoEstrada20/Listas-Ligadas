# Clase que representa una canción
class Cancion:
    # Método constructor de la clase Cancion
    def __init__(self, titulo, artista, album):
        # Inicializa los atributos de la canción
        self.titulo = titulo  # Título de la canción
        self.artista = artista  # Artista de la canción
        self.album = album  # Álbum al que pertenece la canción

    # Método que devuelve una representación en cadena de la canción
    def __str__(self):
        return f"Canción: {self.titulo} \nInterpretada por: {self.artista} \nDel álbum: {self.album}\n"


# Clase que representa un nodo en la lista enlazada (playlist)
class Nodo:
    # Método constructor de la clase Nodo
    def __init__(self, cancion):
        self.cancion = cancion  # Contiene un objeto de tipo Cancion
        self.siguiente = None  # Referencia al siguiente nodo en la lista, inicialmente es None


# Clase que representa la playlist como una lista enlazada
class Playlist:
    # Método constructor de la clase Playlist
    def __init__(self):
        self.cabeza = None  # Inicializa la cabeza de la lista enlazada, al principio no hay canciones

    # Método para agregar una canción a la playlist
    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)  # Crea un nuevo nodo con la canción proporcionada
        if self.cabeza is None:  # Si la playlist está vacía, la nueva canción será la cabeza
            self.cabeza = nuevo_nodo
        else:
            ultimo_nodo = self.cabeza  # Si no está vacía, busca el último nodo
            while ultimo_nodo.siguiente:  # Itera hasta encontrar el último nodo
                ultimo_nodo = ultimo_nodo.siguiente
            ultimo_nodo.siguiente = nuevo_nodo  # Enlaza el último nodo con el nuevo nodo

    # Método para eliminar una canción de la playlist por su título
    def eliminar_cancion(self, titulo):
        actual = self.cabeza  # Comienza en la cabeza de la lista
        previo = None  # Mantiene referencia al nodo anterior al nodo actual

        # Busca la canción en la lista
        while actual and actual.cancion.titulo != titulo:
            previo = actual
            actual = actual.siguiente

        if actual is None:  # Si no se encuentra la canción
            print(f"La canción '{titulo}' no se encuentra en la playlist.\n")
            return

        if previo is None:  # Si la canción a eliminar es la cabeza de la lista
            self.cabeza = actual.siguiente  # La nueva cabeza será el siguiente nodo
        else:
            previo.siguiente = actual.siguiente  # El nodo anterior ahora apunta al siguiente del nodo actual

    # Método para mostrar todas las canciones de la playlist
    def mostrar_playlist(self):
        nodo_actual = self.cabeza  # Comienza en la cabeza de la lista
        while nodo_actual:  # Itera a través de todos los nodos de la lista
            print(nodo_actual.cancion)  # Muestra la canción actual (usando __str__)
            nodo_actual = nodo_actual.siguiente  # Pasa al siguiente nodo
        print("\nFin de la playlist\n")  # Indica el final de la lista


# Ejemplo de uso de la clase Playlist y Cancion
playlist = Playlist()  # Crea una nueva playlist
cancion1 = Cancion("Jesus Of Suburbia", "Green Day", "American Idiot")  # Crea una nueva canción
cancion2 = Cancion("New Divide", "Linkin Park", "Papercuts")
cancion3 = Cancion("Black", "Pearl Jam", "Ten")
cancion4 = Cancion("Basket Case", "Green Day", "Dookie")
cancion5 = Cancion("Be Quiet and Drive (Far Away)", "Deftones", "Around the Fur")
cancion6 = Cancion("ATWA", "System Of A Down", "Toxicity")
cancion7 = Cancion("Best Of You", "Foo Fighters", "In Your Honor")

playlist.agregar_cancion(cancion1)  # Agrega la canción a la playlist
playlist.agregar_cancion(cancion2)  
playlist.agregar_cancion(cancion3)  
playlist.agregar_cancion(cancion4)  
playlist.agregar_cancion(cancion5)  
playlist.agregar_cancion(cancion6)  
playlist.agregar_cancion(cancion7)  


playlist.mostrar_playlist()  # Muestra todas las canciones de la playlist

playlist.eliminar_cancion("Best Of You")  # Elimina la canción de la playlist
playlist.mostrar_playlist()  # Muestra todas las canciones restantes de la playlist

playlist.eliminar_cancion("Beware")  # Intenta eliminar una canción que no está en la playlist
