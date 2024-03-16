## Búsqueda en Profundidad (DFS) - Resultados

## Iteración 0:
- **Frontera**: ['I', 'E', 'D']
- **Nodos Expandidos**: ['A']

En la primera iteración, partiendo del nodo inicial 'A', exploramos sus vecinos 'I', 'E' y 'D'. El nodo 'A' se marca como expandido.

## Iteración 1:
- **Frontera**: ['I', 'E', 'J', 'I', 'B']
- **Nodos Expandidos**: ['A', 'D']

En la segunda iteración, el nodo 'D' se expande y se añaden a la frontera sus vecinos 'I', 'J' y 'B'.

## Iteración 2:
- **Frontera**: ['I', 'E', 'J', 'I', 'F', 'E']
- **Nodos Expandidos**: ['A', 'D', 'B']

La frontera se expande aún más con los vecinos de 'E': 'I', 'F' y 'H'.

## Iteración 3:
- **Frontera**: ['I', 'E', 'J', 'I', 'F', 'H', 'F']
- **Nodos Expandidos**: ['A', 'D', 'B', 'E']

La exploración continúa con los nodos 'F' y 'H' de la frontera.

## Iteración 4:
- **Frontera**: ['I', 'E', 'J', 'I', 'F', 'H', 'Z', 'H']
- **Nodos Expandidos**: ['A', 'D', 'B', 'E', 'F']

El nodo 'F' se expande y se descubre el nodo de destino 'Z', que se añade a la frontera.

## Iteración 5:
- **Frontera**: ['I', 'E', 'J', 'I', 'F', 'H', 'Z', 'Z', 'K']
- **Nodos Expandidos**: ['A', 'D', 'B', 'E', 'F', 'H']

La frontera incluye ahora los vecinos del nodo 'H', incluyendo nuevamente 'Z'.

## Iteración 6:
- **Frontera**: ['I', 'E', 'J', 'I', 'F', 'H', 'Z', 'Z']
- **Nodos Expandidos**: ['A', 'D', 'B', 'E', 'F', 'H', 'K']

En esta etapa, el nodo 'H' se expande y 'K' se añade a la frontera.

## Iteración 7:
- **Nodo de Destino Encontrado: Z**

La búsqueda se detiene ya que el nodo de destino 'Z' ha sido encontrado.

Este proceso muestra cómo la búsqueda en profundidad explora el grafo desde el nodo inicial 'A' hasta encontrar el nodo de destino 'Z', expandiendo nodos y actualizando la frontera en cada iteración.
