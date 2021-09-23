# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from automata.fa.dfa import DFA
qtCreatorFile = "untitled.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.ok.clicked.connect(self.calculos)
    def calculos (self):
        totalacumulado = 0
        bill1 = (self.m1.value())
        bill2 = (self.m2.value())
        bill3 = (self.m3.value())
        temp1 = bill1
        temp2 = bill2
        temp3 = bill3
        if bill1 > 0:
            un = "1"
        else:
            un = ""
        while temp1 > 1:
            temp1 = temp1 - 1
            un = "1" + un
        if bill2 > 0:
            un2 = "2"
        else:
            un2 = ""
        while temp2 > 1:
            temp2 = temp2 - 1
            un2 = "2" + un2
        if bill3 > 0:
            un3 = "5"
        else:
            un3 = ""
        while temp3 > 1:
            temp3 = temp3 - 1
            un3 = "5" + un3
        totalacumulado = (bill1*1000)+(bill2*2000)+(bill3*5000)
        total =  str(totalacumulado)
        self.total.setText(total)
        producto = (self.producto.currentText())
        if producto == 'Empanada':
            q = "a"
        if producto == 'Sandwich':
            q = "b"
        if producto == 'Perro caliente y naranjada':
            q = "c"
        if producto == 'Papas locas y limonada':
            q = "d"
        if producto == 'Hamburguesa y coca-cola':
            q = "e"
        dfa1 = DFA(
        states={'q0', 'q1', 'q2', 'q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13'},
        input_symbols={'a', 'b','c','d','e','1','2','5'},
        transitions={
        'q0': {'a': 'q1', 'b': 'q5', 'c':'q9', 'd':'q11', 'e':'q12'},
        'q1': {'1': 'q2', '2': 'q3', '5':'q4'},
        'q2': {},
        'q3': {},
        'q4': {},
        'q5': {'1': 'q6', '2': 'q1', '5':'q8'},
        'q6': {'1': 'q1', '2': 'q2', '5':'q7'},
        'q7': {},
        'q8': {},
        'q9': {'1': 'q10', '2': 'q5', '5':'q2'},
        'q10': {'1': 'q5', '2': 'q6', '5':'q3'},
        'q11': {'1': 'q9', '2': 'q10', '5':'q1'},
        'q12': {'1': 'q13', '2':'q11', '5':'q5'},
        'q13': {'1': 'q11', '2': 'q9', '5':'q6'}
         },
        initial_state='q0',
        final_states={'q2','q3','q4','q7','q8'}
        ) 
        try:
            validar = dfa1.validate_input(q+un+un2+un3)
        except Exception as e:
            print("No tiene suficiente dinero")
        if validar == 'q2':
            validar2 = '0' 
        if validar == 'q3':
            validar2 = '1000'
        if validar == 'q4':
            validar2 = '4000'
        if validar == 'q7':
            validar2 = '3000'
        if validar == 'q8':
            validar2 = '2000'
        self.total2.setText(validar2)
    def show_dialog(self):
        dialog = Dialog(self)  # self hace referencia al padre
        dialog.show()
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
