class Cliente:
    def __init__(self, nombre, unidadFamiliar, telefono, habitacionAsignada, estado):
        self.nombre = nombre
        self.unidadFamiliar = unidadFamiliar
        self.telefono = telefono
        self.habitacionAsignada = habitacionAsignada
        self.estado = estado

        self.descripcion = "Nombre: "+self.nombre+"\nUnidad familiar: "+str(self.unidadFamiliar)+"\nTeléfono: "+str(self.telefono)+"\nHabitación asignada: "+str(self.habitacionAsignada)+"\nEstado: "+self.estado+"\n"

class Habitacion:
    def __init__(self, nombre, numeroCamas, estado):
        self.nombre = nombre
        self.numeroCamas = numeroCamas
        self.estado = estado

        self.descripcion = "Nombre: "+self.nombre+"\nNúmero de camas: "+str(self.numeroCamas)+"\nEstado: "+self.estado+"\n"


clientes=[
    Cliente("Rafa", 4, 957453676, "Habitación 1", "Pendiente"),
    Cliente("Laura", 3, 957453236, "Habitación 7", "Pendiente"),
    Cliente("Marcos", 3, 957445476, "Habitación 2", "Pendiente"),
    Cliente("David", 2, 957458726, "Habitación 5", "Pendiente"),
    Cliente("Alba", 5, 957452276, "Habitación 3", "Pendiente"),
    Cliente("Jesus", 1, 957111676, "Habitación 6", "Pendiente"),
    Cliente("Silvia", 1, 957453600, "Habitación 4", "Pendiente"),
]

habitaciones=[
    Habitacion("Habitación 1", 5, "Sin completar"),
    Habitacion("Habitación 2", 3, "Sin completar"),
    Habitacion("Habitación 3", 4, "Sin completar"),
    Habitacion("Habitación 4", 5, "Sin completar"),
    Habitacion("Habitación 5", 2, "Sin completar"),
    Habitacion("Habitación 6", 1, "Sin completar"),
    Habitacion("Habitación 7", 2, "Sin completar"),
    Habitacion("Habitación 8", 3, "Sin completar"),
]