from bcPlanificacion import *

# Nodeo de la red de estadios
class EstadioSpain(Node):
    def __init__(self, id, connections, type, name):
        Node.__init__(self, id, connections, type)
        self.name = name


# Grafo de los estadios
class EstadiosPlan(Graph):
    def __init__(self, name, id, nodes):
        Graph.__init__(self, nodes)
        self.name = name
        self.id = id
        self.nodes = nodes

    def __repr__(self):
        recorrido = str(self.nodes).strip("[]")  # Eliminamos los corchetes del array
        return "El " + str(self.name) + " recorre: " + str(self.getCost()) + " kilometros: " + recorrido + "\n"