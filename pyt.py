import sqlite3; from PyQt5.uic import loadUi; from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets; import sys
class Inicio(QDialog):
    def __init__(self):
        super(Inicio, self).__init__()
        loadUi("Login.ui", self)
        self.lne_contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_iniciarSesion.clicked.connect(self.inicioSesion)

    def inicioSesion(self):
        user = self.lne_usuario.text()
        pw = self.lne_contrasena.text()
        
        con = sqlite3.connect("asd.sqlite")
        cursor = con.cursor()
        if user == "" and pw == "": self.lbl_alerta.setText("Campos vacios...")
        elif user != "" and pw != "":
            try:
                sql = "SELECT * FROM cuentas WHERE USUARIO = \""+user+'\"'
                cursor.execute(sql)
                res = cursor.fetchall()
                if user == res[0][0] and pw == res[0][1]:
                    trabajador = Trabajador()
                    widget.addWidget(trabajador)
                    widget.setFixedWidth(930)
                    widget.setFixedHeight(630)
                    widget.setCurrentIndex(widget.currentIndex()+1)   
                else:  
                    self.lbl_alerta.setText("Usuario o contrasena incorrectos")
            except IndexError:
                self.lbl_alerta.setText("Usuario o contrasena incorrectos")
            
        elif user == "":    self.lbl_alerta.setText("Campo usuario vacio")
        elif pw == "": self.lbl_alerta.setText("Campo contrasena vacio")



class Trabajador(QDialog):
    def __init__(self):
        super(Trabajador, self).__init__()
        loadUi("Trabajador.ui", self)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)
        con = sqlite3.connect("asd.sqlite")
        cursor = con.cursor()
        self.btn_registrar.clicked.connect(self.registrar_pasajeros)
        self.btn_actualizar.clicked.connect(self.actualizar)
        sql = "SELECT * FROM pasajeros"
        cursor.execute(sql)
        c = len(cursor.fetchall())

        self.tabla.setRowCount(c)
        fila = 0
        for i in cursor.execute(sql):
            self.tabla.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tabla.setItem(fila, 1, QtWidgets.QTableWidgetItem(i[1]))
            self.tabla.setItem(fila, 2, QtWidgets.QTableWidgetItem(i[2]))
            self.tabla.setItem(fila, 3, QtWidgets.QTableWidgetItem(i[3]))
            self.tabla.setItem(fila, 4, QtWidgets.QTableWidgetItem(i[4]))
            self.tabla.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(i[5])))
            self.tabla.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(i[6])))
            self.tabla.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(i[7])))
            fila+=1

        lista = ['1','2','3','4','5','6','7','8','9','10']

        self.b1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pasajeros))
        self.b2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.registrar))
        self.b3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.habitacion))


        for i in lista:
            self.habitaciones.addItem(i)

    def registrar_pasajeros(self):
        con = sqlite3.connect("asd.sqlite")
        cursor = con.cursor()
        rut = self.lne_rut.text()
        nombre = self.lne_nombre.text()
        apellido = self.lne_apellido.text()
        correo = self.lne_correo.text()
        telefono = self.lne_telefono.text()
        habitacion = self.habitaciones.currentText()
        encargado = self.encargado.isChecked()

        if encargado == True:   encargado = 1
        else: encargado == 0

        sql = f"INSERT INTO pasajeros (RUT, NOMBRE, APELLIDO, CORREO, TELEFONO, HABITACION, ENCARGADO)\
             VALUES ('{rut}', '{nombre}', '{apellido}', '{correo}', {telefono}, {habitacion}, {encargado})"
        cursor.execute(sql)
        con.commit()
        con.close()

    def actualizar(self):
        con = sqlite3.connect("asd.sqlite")
        cursor = con.cursor()
        sql = "SELECT * FROM pasajeros"
        cursor.execute(sql)
        c = len(cursor.fetchall())

        self.tabla.setRowCount(c)
        fila = 0
        for i in cursor.execute(sql):
            self.tabla.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tabla.setItem(fila, 1, QtWidgets.QTableWidgetItem(i[1]))
            self.tabla.setItem(fila, 2, QtWidgets.QTableWidgetItem(i[2]))
            self.tabla.setItem(fila, 3, QtWidgets.QTableWidgetItem(i[3]))
            self.tabla.setItem(fila, 4, QtWidgets.QTableWidgetItem(i[4]))
            self.tabla.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(i[5])))
            self.tabla.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(i[6])))
            self.tabla.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(i[7])))
            fila+=1
        
    def checked(self):
        print(self.encargado.isChecked())
a = 1
app = QApplication(sys.argv)
inicio = Inicio()
widget = QtWidgets.QStackedWidget()
widget.addWidget(inicio)
widget.setFixedWidth(400)
widget.setFixedHeight(420)
widget.show()
app.exec_()