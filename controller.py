import model as model

def asignacion(domain):
    lista = model.asignacionObjetos(domain)
    return lista

def getObjetosCitas():
    objetos = model.getObjetosCitas()
    return objetos

def getDescripcionObjetosCitas(nombre):
    objetos = model.getDescripcionObjetosCitas(nombre)
    return objetos

def getRecursosCitas():
    recursos = model.getRecursosCitas()
    return recursos

def getDescripcionRecursosCitas(nombre):
    recursos = model.getDescripcionRecursosCitas(nombre)
    return recursos

def getObjetosHotel():
    objetos = model.getObjetosHotel()
    return objetos

def getDescripcionObjetosHotel(nombre):
    objetos = model.getDescripcionObjetosHotel(nombre)
    return objetos

def getRecursosHotel():
    recursos = model.getRecursosHotel()
    return recursos

def getDescripcionRecursosHotel(nombre):
    recursos = model.getDescripcionRecursosHotel(nombre)
    return recursos
