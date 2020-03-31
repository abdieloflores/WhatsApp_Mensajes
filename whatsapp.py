# -*- coding: utf-8 -*-
import sys
import webbrowser
import Iconos.iconos
from PyQt5 import QtWidgets,uic

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainWindow,self).__init__()
        uic.loadUi('interfaz/mainWindow.ui',self)
        self.show()
        self.enviar.clicked.connect(self.envio)

    def envio(self):
        self.telefono = str(self.line_telefono.text())
        self.mensaje = str(self.line_mensaje.text())
        self.pagina = "https://api.whatsapp.com/send?phone=%s&text=%s" % (self.telefono,self.mensaje)
        webbrowser.open_new(self.pagina)


app = QtWidgets.QApplication(sys.argv)
window = mainWindow()
app.exec()