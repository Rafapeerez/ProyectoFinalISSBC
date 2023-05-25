class Objeto:
    def __init__(self, nombre, identificador, estado, caract1, caract2, caract3):
        self.nombre = nombre
        self.id = identificador
        self.estado = estado
        self.caract1 = caract1
        self.caract2 = caract2
        self.caract3 = caract3


class Recurso:
    def __init__(self, nombre, identificador, estado, caract1, caract2, caract3, cantidad):
        self.nombre = nombre
        self.id = identificador
        self.estado = estado
        self.caract1 = caract1
        self.caract2 = caract2
        self.caract3 = caract3
        self.cantidad = cantidad


recursos = [
    Recurso("despacho", 1, "No asignado", ["tamanio", 2], ["ventanas", 2], ["equipo", 2], 1),
    Recurso("despacho", 2, "No asignado", ["tamanio", 3], ["ventanas", 3], ["equipo", 3], 2),
    Recurso("despacho", 3, "No asignado", ["tamanio", 4], ["ventanas", 4], ["equipo", 4], 3),
    Recurso("despacho", 4, "No asignado", ["tamanio", 5], ["ventanas", 4], ["equipo", 4], 3),
    Recurso("despacho", 5, "No asignado", ["tamanio", 5], ["ventanas", 4], ["equipo", 10], 3)
]

objetos = [
    Objeto("Juan", 1, "Sin recurso", ["becario", 1], ["grado", 6], ["articulos_publicados", 103]),
    Objeto("Pedro", 2, "Sin recurso", ["becario", 1], ["grado", 6], ["articulos_publicados", 108]),
    Objeto("Maria", 3, "Sin recurso", ["becario", 1], ["grado", 6], ["articulos_publicados", 93]),
    Objeto("Antonio", 11, "Sin recurso", ["catedratico", 80], ["grado", 6], ["articulos_publicados", 30]),
    Objeto("Jesus", 12, "Sin recurso", ["catedratico", 80], ["grado", 6], ["articulos_publicados", 26]),
    Objeto("Aurora", 13, "Sin recurso", ["catedratico", 80], ["grado", 6], ["articulos_publicados", 22]),
    Objeto("Laura", 14, "Sin recurso", ["catedratico", 80], ["grado", 6], ["articulos_publicados", 12]),
    Objeto("Manuel", 21, "Sin recurso", ["profesor_adjunto", 10], ["grado", 6], ["articulos_publicados", 98]),
    Objeto("Jose", 22, "Sin recurso", ["profesor_adjunto", 10], ["grado", 6], ["articulos_publicados", 97]),
    Objeto("Francisco", 23, "Sin recurso", ["profesor_adjunto", 10], ["grado", 6], ["articulos_publicados", 80])
]


def asignar_recurso(objeto, recurso):
    objeto.estado = "Asignado"
    recurso.estado = "Asignado"


def regla1(objeto, recurso):
    if objeto.caract1[1] >= recurso.caract1[1] and objeto.caract2[1] >= recurso.caract2[1] and objeto.caract3[1] >= recurso.caract3[1]:
        asignar_recurso(objeto, recurso)
        print(f"Se ha asignado el recurso {recurso.id} a {objeto.nombre}.")


def regla2(objeto, recurso):
    if objeto.estado == "Sin recurso" and recurso.estado == "No asignado":
        asignar_recurso(objeto, recurso)
        print(f"Se ha asignado el recurso {recurso.id} a {objeto.nombre}.")


# Ejecutar las reglas para asignar los recursos a los objetos
for objeto in objetos:
    for recurso in recursos:
        regla1(objeto, recurso)
        regla2(objeto, recurso)
