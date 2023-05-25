class Paciente:
    def __init__(self, nombre, edad, telefono, doctorAsignado, estado):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.doctorAsignado = doctorAsignado
        self.estado = estado

    def InstaciasPacientes(pacientes):
        return pacientes

class Doctor:
    def __init__(self, nombre, consulta, horario, estado):
        self.nombre = nombre
        self.consulta = consulta
        self.horario = horario
        self.estado = estado


pacientes=[
    Paciente("Rafa", 76, 957453676, "Dr. Fernandez", "Pendiente"),
    Paciente("Marcos", 34, 957445476, "Dr. Reina", "Pendiente"),
    Paciente("Alba", 69, 957452276, "Dr. Caballero", "Pendiente"),
    Paciente("Silvia", 12, 957453600, "Dr. Caballero", "Pendiente"),
    Paciente("David", 45, 957458726, "Dr. Luque", "Pendiente"),
    Paciente("Jesus", 35, 957111676, "Dr. Fernandez", "Pendiente"),
    Paciente("Laura", 62, 957453236, "Dr. Reina", "Pendiente"),
]

doctores=[
    Doctor("Dr. Fernandez", "Consulta 1", ["Lunes 20/05 9:00", "Martes 21/05 10:30", "Miércoles 22/05 12:00"], "Sin completar"),
    Doctor("Dr. Reina", "Consulta 2", ["Lunes 20/05 9:00", "Martes 21/05 10:30"], "Sin completar"),
    Doctor("Dr. Caballero", "Consulta 3", [], "Sin completar"),
    Doctor("Dr. Luque", "Consulta 4", ["Lunes 20/05 9:00", "Martes 21/05 10:30, Miércoles 22/05 12:00"], "Sin completar"),
]


