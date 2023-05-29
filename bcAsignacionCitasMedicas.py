class Paciente:
    def __init__(self, nombre, edad, telefono, doctorAsignado, estado):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.doctorAsignado = doctorAsignado
        self.estado = estado

        self.descripcion = "Nombre: "+self.nombre+"\nEdad: "+str(self.edad)+"\nTeléfono: "+str(self.telefono)+"\nDoctor asignado: "+self.doctorAsignado+"\nEstado: "+self.estado+"\n"

class Doctor:
    def __init__(self, nombre, consulta, horario, estado):
        self.nombre = nombre
        self.consulta = consulta
        self.horario = horario
        self.estado = estado

        self.descripcion = "Nombre: "+self.nombre+"\nConsulta asignada: "+str(self.consulta)+"\nHorario: "+str(self.horario)+"\nEstado: "+self.estado+"\n"


pacientes=[
    Paciente("Rafa", 76, 957453676, "Dr. Fernandez", "Pendiente"),
    Paciente("Carlitos", 34, 957445476, "Dr. Pérez", "Pendiente"),
    Paciente("Alba", 69, 957452276, "Dr. Caballero", "Pendiente"),
    Paciente("Silvia", 12, 957453600, "Dr. Caballero", "Pendiente"),
    Paciente("David", 45, 957458726, "Dr. Luque", "Pendiente"),
    Paciente("Jesus", 35, 957111676, "Dr. Fernandez", "Pendiente"),
    Paciente("Laura", 62, 957453236, "Dr. Pérez", "Pendiente"),
]

doctores=[
    Doctor("Dr. Fernandez", "Consulta 1", ["Miércoles 31/05 9:00", "Jueves 01/06 10:30", "Viernes 02/06 12:50"], "Sin completar"),
    Doctor("Dr. Pérez", "Consulta 2", ["Martes 30/05 11:25", "Miércoles 31/05 9:00"], "Sin completar"),
    Doctor("Dr. Caballero", "Consulta 3", [], "Asignado"),
    Doctor("Dr. Luque", "Consulta 4", ["Martes 30/05 12:45", "Jueves 01/06 8:30"], "Sin completar"),
]