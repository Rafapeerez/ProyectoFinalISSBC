import time
from PyQt5.QtWidgets import *
import sys

import controller as controller

class Asignador(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        #Cargamos las opciones del dominio. Si este cambia, se vuelven a cargar
        self.loadDomain(self.comboDomain.currentText())
        self.comboDomain.currentTextChanged.connect(self.loadDomain)
    
    def initUI(self):
        #Títulos de las secciones
        selector = QLabel("Seleccione el dominio deseado:")
        objetos = QLabel("Usuarios")
        descripcionUsuarios = QLabel("Descripción detallada")
        recursos = QLabel("Recursos")
        descripcionRecursos = QLabel("Descripción detallada")
        asignacionFinal = QLabel("Asignación realizada:")

        # Listas de objetos y recursos con sus descripciones
        self.objetos = QListWidget()
        self.recursos = QListWidget()
        self.descripcionUsuarios = QTextEdit()
        self.descripcionRecursos = QTextEdit()
        self.asignacionFinalTexto = QListWidget()

        #Se crea un botón para asignar tareas
        self.assignButton = QPushButton("Asignar")

        # Creamos el combo para elegir el dominio
        self.comboDomain = QComboBox()
        self.comboDomain.addItem("Asignación de Citas Médicas")
        self.comboDomain.addItem("Asignación de Habitaciones de Hotel")

        # Creamos un diseño vertical donde añadimos el horizontal que hemos creado previamente
        vbox = QVBoxLayout()
        vbox.setSpacing(30)
        vbox.addWidget(selector)
        vbox.addWidget(self.comboDomain)

        # Creamos una cuadrícula donde añadiremos los componentes de la seccion de archivo especificando sus coordenadas
        grid = QGridLayout()
        grid.setSpacing(10)

        # Añadimos los componentes a la cuadrícula en bloques de dos, cada uno con su descripcion.
        grid.addWidget(objetos, 0, 0)
        grid.addWidget(self.objetos, 1, 0)
        grid.addWidget(descripcionUsuarios, 0, 1)
        grid.addWidget(self.descripcionUsuarios, 1, 1)
        grid.addWidget(recursos, 2, 0)
        grid.addWidget(self.recursos, 3, 0)
        grid.addWidget(descripcionRecursos, 2, 1)
        grid.addWidget(self.descripcionRecursos, 3, 1)

        #El boton de asignar ocupa todo el ancho de la cuadrícula
        grid.addWidget(self.assignButton, 4, 0, 1, 2)

        #Se añade un espacio en blanco para separar la asignación de la descripción de la misma
        grid.addWidget(QLabel(""), 5, 0)
        grid.addWidget(asignacionFinal, 6, 0)
        grid.addWidget(self.asignacionFinalTexto, 7, 0, 1, 2)

        # Añadir el diseño de cuadricula de archivos al diseño vertical
        vbox.addLayout(grid)

        self.assignButton.clicked.connect(lambda: self.asignar(self.comboDomain.currentText()))

        #Se establece el tamaño de la ventana y se muestra
        self.setLayout(vbox)
        self.setGeometry(300, 1300, 1100, 850)
        self.setWindowTitle('Asignador de Tareas')
        self.show()

    # Carga el dominio que hayamos seleccionado en el combo
    def loadDomain(self, domain):
        #Se limpian las listas de objetos y recursos
        self.objetos.clear()
        self.recursos.clear()

        if domain =="Asignación de Citas Médicas":
            self.descripcionUsuarios.clear()
            self.descripcionRecursos.clear()
            self.asignacionFinalTexto.clear()

            #Se recorren todos los pacientes y se añaden a la lista de objetos
            self.objetos.addItems(controller.getObjetosCitas())
            #Si se selecciona un nombre, se muestra su descripción es self.descripcionUsuarios
            self.objetos.itemClicked.connect(lambda: self.descripcionUsuarios.setText(controller.getDescripcionObjetosCitas(self.objetos.currentItem().text())))

            #Se recorren todos los médicos y se añaden a la lista de recursos
            self.recursos.addItems(controller.getRecursosCitas())
            #Si se selecciona un nombre, se muestra su descripción es self.descripcionRecursos
            self.recursos.itemClicked.connect(lambda: self.descripcionRecursos.setText(controller.getDescripcionRecursosCitas(self.recursos.currentItem().text())))
        
        elif domain == "Asignación de Habitaciones de Hotel":
            self.descripcionUsuarios.clear()
            self.descripcionRecursos.clear()
            self.asignacionFinalTexto.clear()
            #Se recorren todos los clientes y se añaden a la lista de objetos
            self.objetos.addItems(controller.getObjetosHotel())
            #Si se selecciona un nombre, se muestra su descripción es self.descripcionUsuarios
            self.objetos.itemClicked.connect(lambda: self.descripcionUsuarios.setText(controller.getDescripcionObjetosHotel(self.objetos.currentItem().text())))

            #Se recorren todas las habitaciones y se añaden a la lista de recursos
            self.recursos.addItems(controller.getRecursosHotel())
            #Si se selecciona un nombre, se muestra su descripción es self.descripcionRecursos
            self.recursos.itemClicked.connect(lambda: self.descripcionRecursos.setText(controller.getDescripcionRecursosHotel(self.recursos.currentItem().text())))

    # Método que se ejecuta cuando se pulsa el botón de asignar
    def asignar(self, domain):

        #self.asignacionFinalTexto.setPlainText("Asignando... \nDominio Seleccionado: " + domain + "Asignaciones: " +"\n¡Objetos y recursos asignados correctamente!")
        self.asignacionFinalTexto.clear()
        self.asignacionFinalTexto.addItem("Asignando...")
        self.asignacionFinalTexto.addItem("----------------------------------------------------------------------")
        self.asignacionFinalTexto.addItem("Dominio Seleccionado: " + domain)
        self.asignacionFinalTexto.addItem("----------------------------------------------------------------------")

        self.asignacionFinalTexto.addItems(controller.asignacion(domain))
        self.asignacionFinalTexto.addItem("----------------------------------------------------------------------")
        self.asignacionFinalTexto.addItem("¡Objetos y recursos asignados correctamente!")
        

    # Método que se despliega cuando se intenta cerrar la app
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Confirmación", "¿Desea cerrar el asignador?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Asignador()
    sys.exit(app.exec_())