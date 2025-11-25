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

    def eliminar(self, id):
        actual = self.cabeza
        previo = None
        while actual:
            if actual.tarea.id == id:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            previo = actual
            actual = actual.siguiente
        return False

    def marcar_completada(self, id):
        actual = self.cabeza
        while actual:
            if actual.tarea.id == id:
                actual.tarea.marcar_completada()
                return True
            actual = actual.siguiente
        return False

class Tarea:
    def __init__(self, id, descripcion):
        self.id = id
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "✔️" if self.completada else "❌"
        return f"{self.id}: {self.descripcion} [{estado}]"

if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.agregar(Tarea(1, "Estudiar Python"))
    lista.agregar(Tarea(2, "Practicar JavaScript"))
    lista.agregar(Tarea(3, "Leer sobre ciencia de datos"))

    print("Listado inicial:")
    lista.listar()

    print("\nMarcando tarea 2 como completada...")
    lista.marcar_completada(2)
    lista.listar()

    print("\nEliminando tarea 1...")
    lista.eliminar(1)
    lista.listar()
