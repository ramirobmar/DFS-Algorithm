## Algoritmo de Búsqueda No Informada: Búsqueda en Profundidad (DFS)
### Descripción:

El algoritmo de búsqueda en profundidad, también conocido como Depth-First Search (DFS) en inglés, es un algoritmo de búsqueda no informada que se utiliza para recorrer o buscar elementos en un grafo o árbol. Es llamado "en profundidad" porque explora tanto lejos como sea posible a lo largo de cada rama antes de retroceder.
Funcionamiento:

El algoritmo comienza explorando un nodo raíz y luego se mueve hacia abajo en profundidad lo más posible a lo largo de cada rama antes de retroceder. Esencialmente, sigue un camino hasta que alcanza un nodo sin nodos vecinos no descubiertos, momento en el cual retrocede al nodo anterior y continúa explorando otros nodos.

### Estructuras de Datos Utilizadas:

Grafo: Representa la estructura de datos principal que contiene los nodos (vértices) y las conexiones entre ellos (aristas).
Frontera: Es una lista que contiene los nodos que se deben explorar. El algoritmo utiliza esta lista para realizar un seguimiento de los nodos que aún no se han explorado.
Nodos Expandidos: Es una lista que contiene los nodos que ya han sido explorados.

### Pasos del Algoritmo:

Inicializar el grafo, la frontera y la lista de nodos expandidos.
Comenzar desde el nodo inicial (raíz) y explorar sus nodos vecinos.
Agregar los nodos vecinos no descubiertos a la frontera.
Extraer un nodo de la frontera y repetir los pasos 2 y 3 hasta que se encuentre el nodo de destino o la frontera esté vacía.

### Beneficios:

Complejidad Espacial Baja: Requiere una cantidad de memoria proporcional a la profundidad máxima del árbol.
Fácil Implementación: Es relativamente sencillo de implementar y entender.
Útil para Grafos Grandes: Puede ser útil para grafos grandes con profundidades limitadas.

### Limitaciones:

Puede Quedar Atrapado en Ciclos: Si se usa sin precaución, puede quedar atrapado en ciclos infinitos si el grafo contiene ciclos.
No Garantiza la Solución Óptima: No garantiza encontrar la solución óptima para problemas como la búsqueda de rutas más cortas.

 
