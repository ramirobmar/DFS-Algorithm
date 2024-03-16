nodes = ["A", "B", "D", "E", "F", "H", "I", "J", "K", "Z"]

# Creamos un diccionario para mantener un registro de qué nodos han sido descubiertos
_discovered = {node: False for node in nodes}

# Definimos la clase Graph para representar un objeto grafo
class Graph:
    def __init__(self, edges, nodes):
        # Inicializamos un diccionario para representar una lista de adyacencia
        self.adjList = {node: [] for node in nodes}
        # Agregamos las aristas al grafo no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

    # Método para obtener los nodos vecinos de un nodo dado
    def get_frontera(self, _nodo):
        # Convertimos la lista de nodos vecinos a un conjunto para eliminar duplicados
        return list(set(self.adjList[_nodo]))

# Definimos la clase Frontera para mantener una lista de nodos frontera
class Frontera:
    def __init__(self, nodes):
        # Inicializamos la lista de frontera con los nodos dados
        self.lista = list(nodes)

    # Método para agregar una lista de nodos a la frontera
    def add_list(self, _lista):
        self.lista.extend(_lista)

    # Método para obtener la lista actual de nodos en la frontera
    def get_list(self):
        return self.lista

    # Método para extraer un nodo de la frontera
    def extract_list(self):
        # Extraemos un nodo de la frontera (si la lista no está vacía)
        if self.lista:
            return self.lista.pop()
        else:
            return None

# Definimos la clase Expandidos para mantener una lista de nodos expandidos
class Expandidos:
    def __init__(self):
        self.lista = []

    # Método para agregar una lista de nodos a la lista de expandidos
    def add_list(self, _lista):
        self.lista.extend(_lista)

    # Método para obtener la lista actual de nodos expandidos
    def get_list(self):
        return self.lista

# Definimos la función Expande_Nodos para expandir los nodos no descubiertos en el grafo
def Expande_Nodos(_grafo, _n):
    _list = []
    # Iteramos sobre los nodos vecinos del nodo dado
    for i in _grafo.get_frontera(_n):
        # Si el nodo vecino no ha sido descubierto, lo agregamos a la lista
        if not _discovered[i]:
            _list.append(i)
    # Ordenamos la lista alfabéticamente y la retornamos
    return sorted(_list)

if __name__ == '__main__':
    _start = "A"
    _end = "Z"
    
    # Definimos las aristas del grafo
    edges = [
        ("A", "I"), ("A", "D"), ("A", "E"), ("E", "A"), ("E", "B"), ("E", "H"), ("B", "E"), ("B", "F"),
        ("B", "D"), ("D", "A"), ("D", "A"), ("D", "J"), ("D", "I"), ("J", "I"), ("J", "D"), ("J", "Z"),
        ("F", "B"), ("F", "E"), ("F", "H"), ("F", "Z"), ("H", "F"), ("H", "E"), ("H", "K"), ("H", "Z")
    ]

    # Creamos el grafo a partir de las aristas
    _graph = Graph(edges, nodes)
    _expanded = Expandidos()
    _frontier = Frontera([_start])

    print("Presentacion de Resultados:\n")
    
    IT = 0
    while _frontier.get_list():
        _nodo = _frontier.extract_list()
        # Verificamos si el nodo extraído es el nodo de destino
        if _nodo == _end:
            print("IT", IT, " Nodo: ", _end, " de destino ENCONTRADO")
            break
        # Si el nodo no ha sido descubierto, lo expandimos
        if not _discovered[_nodo]:
            _expanded.add_list([_nodo])
            _discovered[_nodo] = True
            # Expandimos los nodos vecinos del nodo actual y los agregamos a la frontera
            _aux_list = Expande_Nodos(_graph, _nodo)
            _aux_list.sort(reverse=True)  # Ordenar alfabéticamente de forma descendente
            _frontier.add_list(_aux_list)
            # Imprimimos los resultados parciales
            print("IT", IT, "Frontera:", _frontier.get_list(), "Expandidos:", _expanded.get_list())
            IT += 1
        else:
            print("El nodo", _nodo, "ya ha sido descubierto")
