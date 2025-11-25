class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, tarea):
        nuevo = Nodo(tarea)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def listar(self):
        actual = self.cabeza
        while actual:
            print(actual.tarea)
            actual = actual.siguiente

if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.agregar("Estudiar Python")
    lista.agregar("Practicar JavaScript")
    lista.listar()
