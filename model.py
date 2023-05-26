import bcAsignacionCitasMedicas as bcACM
import bcAsignacionHabitacionesHotel as bcAHH

def asignar(objeto, recurso, cita, domain):
    objeto.estado = "Asignado"

    if domain == "Asignación de Citas Médicas":
        if recurso.horario == []:
            recurso.estado = "Asignado"

    elif domain == "Asignación de Habitaciones de Hotel":
        recurso.estado = "Asignado"

    return cita

def regla1(objeto, recurso, domain):
    if domain == "Asignación de Citas Médicas":
        if objeto.doctorAsignado == recurso.nombre and recurso.horario != [] and objeto.estado == "Pendiente":
            asignacion = "El paciente "+objeto.nombre+" tiene una cita con el "+recurso.nombre+" en la "+recurso.consulta+" el día "+recurso.horario[0]

            recurso.horario.remove(recurso.horario[0])
            asignar(objeto, recurso, asignacion, domain)
            return asignacion
    
    elif domain == "Asignación de Habitaciones de Hotel":
        if objeto.habitacionAsignada == recurso.nombre and recurso.numeroCamas >= objeto.unidadFamiliar and objeto.estado == "Pendiente":
            asignacion = "El cliente "+objeto.nombre+" tiene asignada la "+recurso.nombre+" con "+str(recurso.numeroCamas)+" camas"

            asignar(objeto, recurso, asignacion, domain)
            return asignacion
        
def regla2(objeto, recurso, domain):
    if domain == "Asignación de Citas Médicas":
        if objeto.doctorAsignado != recurso.nombre and recurso.horario != []  and objeto.estado == "Pendiente":
            asignacion = "El paciente "+objeto.nombre+" tiene una cita con el "+recurso.nombre+" en la "+recurso.consulta+" el día "+recurso.horario[0]

            recurso.horario.remove(recurso.horario[0])

            asignar(objeto, recurso, asignacion, domain)
            return asignacion

    elif domain == "Asignación de Habitaciones de Hotel":
        if objeto.habitacionAsignada != recurso.nombre and recurso.numeroCamas >= objeto.unidadFamiliar and objeto.estado == "Pendiente":
            asignacion = "El cliente "+objeto.nombre+" tiene asignada la "+recurso.nombre+" con "+str(recurso.numeroCamas)+" camas"

            asignar(objeto, recurso, asignacion, domain)
            return asignacion

def asignacionObjetos(domain):
    list3 = []
    if domain == "Asignación de Citas Médicas":
        for paciente in bcACM.pacientes:
            for doctor in bcACM.doctores:
                asig = regla1(paciente, doctor, domain)
                if asig != None :
                    list3.append(asig)
                if paciente.doctorAsignado == doctor.nombre and doctor.estado == "Asignado":
                    for doctor in bcACM.doctores:
                        asig = regla2(paciente, doctor, domain)
                        if asig != None :
                            list3.append(asig)

    elif domain == "Asignación de Habitaciones de Hotel":
        for cliente in bcAHH.clientes:
            for habitacion in bcAHH.habitaciones:
                asig = regla1(cliente, habitacion, domain)
                if asig != None :
                    list3.append(asig)
                if cliente.habitacionAsignada == habitacion.nombre and habitacion.estado == "Asignado":
                    for habitacion in bcAHH.habitaciones:
                        asig = regla2(cliente, habitacion, domain)
                        if asig != None :
                            list3.append(asig)

    return list3

#Recorre la lista de pacientes y devuelve el nombre de cada uno
def getObjetosCitas():
    nombres = []
    for paciente in bcACM.pacientes:
        nombres.append(paciente.nombre)
    return nombres

#Recorre la lista de pacientes y devuelve la descripcion del paciente seleccionado
def getDescripcionObjetosCitas(nombre):
    for paciente in bcACM.pacientes:
        if paciente.nombre == nombre:
            return paciente.descripcion

def getRecursosCitas():
    nombres = []
    for doctor in bcACM.doctores:
        nombres.append(doctor.nombre)
    return nombres

def getDescripcionRecursosCitas(nombre):
    for doctor in bcACM.doctores:
        if doctor.nombre == nombre:
            return doctor.descripcion

def getObjetosHotel():
    nombres = []
    for cliente in bcAHH.clientes:
        nombres.append(cliente.nombre)
    return nombres

def getDescripcionObjetosHotel(nombre):
    for cliente in bcAHH.clientes:
        if cliente.nombre == nombre:
            return cliente.descripcion

def getRecursosHotel():
    nombres = []
    for habitacion in bcAHH.habitaciones:
        nombres.append(habitacion.nombre)
    return nombres  

def getDescripcionRecursosHotel(nombre):
    for habitacion in bcAHH.habitaciones:
        if habitacion.nombre == nombre:
            return habitacion.descripcion
