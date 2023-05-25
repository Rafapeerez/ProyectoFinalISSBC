import bcAsignacionCitasMedicas as bcACM
import bcAsignacionHabitacionesHotel as bcAHH

def asignar(objeto, recurso):
    objeto.estado = "Asignado"

    if recurso.horario.length() == 0:
        recurso.estado = "Asignado"

def regla1(paciente, doctor):
    if paciente.doctorAsignado == doctor.nombre and doctor.horario.length() > 0 and paciente.estado == "Pendiente":
        print("El paciente"+paciente.nombre+"tiene una cita  el doctor"+doctor.nombre+"en la consulta"+doctor.consulta+"el dia"+doctor.horario[0])
        doctor.horario.pop()
        asignar(paciente, doctor)

def regla2(paciente, doctor):
    if paciente.doctorAsignado != doctor.nombre and doctor.horario.length() > 0  and paciente.estado == "Pendiente":
        print("El paciente"+paciente.nombre+"tiene una cita  el doctor"+doctor.nombre+"en la consulta"+doctor.consulta+"el dia"+doctor.horario[0])
        doctor.horario.pop()
        asignar(paciente, doctor)

def asignacionCitasMedicas():
    for paciente in bcACM.pacientes:
        for doctor in bcACM.doctores:
            regla1(paciente, doctor)
            if paciente.doctorAsignado == doctor.nombre and doctor.estado == "Asignado":
                for doctor in bcACM.doctores:
                    regla2(paciente, doctor)

#Recorre la lista de pacientes y devuelve el nombre de cada uno
def getObjetosCitas():
    for paciente in bcACM.pacientes:
        return paciente.nombre

def getRecursosCitas():
    for doctor in bcACM.doctores:
        return doctor.nombre

def getObjetosHotel():
    return bcAHH.clientes

def getRecursosHotel():
    return bcAHH.habitaciones

