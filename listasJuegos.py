class Juego:
    def __init__(self, nombre,precio,clasificacion):
        self.nombre = nombre  # El nombre del nodo
        self.precio =precio
        self.clasificacion =clasificacion
        self.next = None  # Apunta al siguiente nodo

class ListaJuegos:
    def __init__(self):
        self.head = None  # Inicialmente, la lista está vacía

    # Método para agregar un nodo al final de la lista
    def agregar(self, nombre,precio,clasificacion):
        nuevo_juego = Juego(nombre,precio,clasificacion)  # Crear un nuevo nodo con el dato
        if self.head is None:  # Si la lista está vacía
            self.head = nuevo_juego  # El nuevo nodo será la cabeza
        else:
            actual = self.head
            while actual.next:  # Avanzar hasta el último nodo
                actual = actual.next
                
            actual.next = nuevo_juego  # Enlazar el nuevo nodo al final
    
    # Agregar en una posición específica
    def agregar_en_posicion(self, nombre,precio,clasificacion, posicion):
        nuevo_juego = Juego(nombre,precio,clasificacion)
        if posicion == 0:
            nuevo_juego.next = self.head
            self.head = nuevo_juego
            return

        actual = self.head
        contador = 0
        while actual and contador < posicion - 1:
            actual = actual.next
            contador += 1
        
        if actual is None:
            print("La posición no es válida")
            return
        
        nuevo_juego.next = actual.next
        actual.next = nuevo_juego

    # Método para imprimir la lista
    def imprimir(self):
        actual = self.head
        while actual:
            print("nombre:",actual.nombre,",precio:",actual.precio,",clasificacion:",actual.clasificacion, end=" -> \n ")
            actual = actual.next
    
    def eliminar_en_posicion(self, posicion):
        
        if self.head is None:
            print("La lista está vacía")
            return
    
        actual = self.head

        if posicion == 0:  # Eliminar la cabeza
            self.head = actual.next
            return
    
        contador = 0
        anterior = None
        
        while actual and contador < posicion:
            anterior = actual
            actual = actual.next
            contador += 1

        if actual is None:
            print("La posición no es válida")
            return

        anterior.next = actual.next  # Saltar el nodo a eliminar


lista = ListaJuegos()

lista.agregar("Mario Bros",1000,"todas las edades")
lista.agregar("Metal Slug",1200,"12+")
lista.agregar("Minecraft",450,"todas las edades")
lista.imprimir()
lista.agregar_en_posicion("Fornite","GRATIS","11+",2)
print(" \n Nueva lista: \n")
lista.imprimir()
lista.eliminar_en_posicion(0)
print(" \n Nueva lista: \n")
lista.imprimir()