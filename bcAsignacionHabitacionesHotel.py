class Cliente:
    def __init__(self, nombre, numeroPersonas, telefono, habitacionAsignada, estado):
        self.nombre = nombre
        self.numeroPersonas = numeroPersonas
        self.telefono = telefono
        self.habitacionAsignada = habitacionAsignada
        self.estado = estado

class Habitacion:
    def __init__(self, nombre, numeroHabitacion, numeroCamas, estado):
        self.nombre = nombre
        self.numeroHabitacion = numeroHabitacion
        self.numeroCamas = numeroCamas
        self.estado = estado


clientes=[
    Cliente("Rafa", 4, 957453676, "1", "Pendiente"),
    Cliente("Marcos", 5, 957445476, "2", "Pendiente"),
    Cliente("Alba", 5, 957452276, "3", "Pendiente"),
    Cliente("Silvia", 1, 957453600, "4", "Pendiente"),
    Cliente("David", 2, 957458726, "5", "Pendiente"),
    Cliente("Jesus", 1, 957111676, "6", "Pendiente"),
    Cliente("Laura", 3, 957453236, "7", "Pendiente"),
]

habitaciones=[
    Habitacion("Dr. Fernandez", "1", 5, "Sin completar"),
    Habitacion("Dr. Reina", "2", 5, "Sin completar"),
    Habitacion("Dr. Caballero", "3", 5, "Sin completar"),
    Habitacion("Dr. Luque", "4", 1, "Sin completar"),
    Habitacion("Dr. Caballero", "5", 2, "Sin completar"),
    Habitacion("Dr. Caballero", "6", 1, "Sin completar"),
    Habitacion("Dr. Caballero", "7", 3, "Sin completar"),

]