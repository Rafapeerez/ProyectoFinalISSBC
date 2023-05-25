#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Trabajo Final de Curso ISBC

Aplicación Asignador de Tareas

Con este fichero se lanza la aplicación

Authors: Alba Palomino, Rafael Emilio Pérez, Silvia Roldán

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo se comentarán las funciones
nuevas de este fichero. El resto que aparezcan sin
comentar, habrán sido comentadas en otros ficheros.
"""

import sys
from PyQt5.QtWidgets import QApplication
import view as view

app = QApplication(sys.argv)  # Crea la app
form = view.Asignador()  # Crea el asignador
sys.exit(app.exec_())  # Se inicia la app y se esperan eventos