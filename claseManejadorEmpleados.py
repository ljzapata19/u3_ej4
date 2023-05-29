import numpy as np
from claseEmpleado import Empleado
from claseDePlanta import DePlanta
from claseContratado import Contratado
from claseExterno import Externo
from datetime import datetime
import csv
class ManejadorEmpleados:
    __empleados = None
    __cantidad = int()
    __dimension = int()
    __incremento = 5
    
    def __init__(self, dimension):
        self.__empleados = np.empty(dimension, dtype = Empleado)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregarEmpleado(self, unEmpleado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__empleados.resize(self.__dimension)
        self.__empleados[self.__cantidad] = unEmpleado
        self.__cantidad += 1
    
    def testEmpleados(self):
        dePlanta = open('planta.csv')
        readerPlanta = csv.reader(dePlanta, delimiter = ';')
        cabecera = True
        for fila in readerPlanta:
            if cabecera:
                cabecera = False
            else:
                unEmpleado = DePlanta(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4]), int(fila[5]))
                self.agregarEmpleado(unEmpleado)
                
        contratado = open('contratados.csv')
        readerContratado = csv.reader(contratado, delimiter = ';')
        cabecera = True
        for fila in readerContratado:
            if cabecera:
                cabecera = False
            else:
                unEmpleado = Contratado(int(fila[0]), fila[1], fila[2], fila[3], fila[4], fila[5], int(fila[6]), float(fila[7]))
                self.agregarEmpleado(unEmpleado)
        
        externo = open('externos.csv')
        readerExterno = csv.reader(externo, delimiter = ';')
        cabecera = True
        for fila in readerExterno:
            if cabecera:
                cabecera = False
            else:
                unEmpleado = Externo(int(fila[0]), fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], float(fila[7]), float(fila[8]), float(fila[9]))
                self.agregarEmpleado(unEmpleado)
        
    def getEmpleados(self):
        return self.__empleados
    
    def registrarHoras(self):
        dni_bus = int(input('\nIngresar dni del empleado: '))
        i = 0
        band = False
        while i < len(self.__empleados) and not isinstance(self.__empleados[i], Contratado):
            i += 1
        if i < len(self.__empleados):
            while i < len(self.__empleados) and isinstance(self.__empleados[i], Contratado):
                
                if self.__empleados[i].getDni() == dni_bus:
                    horas_hoy = int(input('Ingrese la cantidad de horas trabajadas hoy: '))
                    self.__empleados[i].aumentarHoras(horas_hoy)
                    self.__empleados[i].imprimirContratado()
                    band = True
                i += 1
            if not band:
                print('Ningun empleado contratado está registrado con ese dni.')
        else:
            print('No existe ningún empleado contratado')
        
    def totalDeTarea(self):
            tarea_bus = input('\nIngresar tarea a buscar: ')
            i = 0
            total = 0
            band = False
            while i < len(self.__empleados) and not isinstance(self.__empleados[i], Externo):
                i += 1
            if i < len(self.__empleados):
                while i < len(self.__empleados) and isinstance(self.__empleados[i], Externo):
                    
                    if self.__empleados[i].getTarea() == tarea_bus:
                        f_fin = datetime.strptime(self.__empleados[i].getFechaFin(), "%Y-%m-%d")
                        fecha_actual = datetime.now()
                        if not (f_fin < fecha_actual):
                            total += self.__empleados[i].getCostoObra()
                            self.__empleados[i].imprimirExterno()
                            band = True
                    i += 1
                if not band:
                    print('\nLa tarea ingresada no existe o ya ha finalizado.')
                else:
                    print('\nEl monto a pagar para la tarea ',tarea_bus,' es: $',total)
    def ayudaEconomica(self):
        i = 0
        while i < self.__cantidad:
            empleado = self.__empleados[i]
            if empleado.calcularSueldo() < 150000:
                print('\n',empleado.calcularSueldo() )
                empleado.imprimirEmpleado()
            i += 1
    def calcularSueldos(self):
        i = 0
        while i < self.__cantidad:
            print('\nNombre: ',self.__empleados[i].getNombre(),'; Telefono: ',self.__empleados[i].getTelefono(),'; Sueldo a cobrar: ',self.__empleados[i].calcularSueldo())
            i += 1