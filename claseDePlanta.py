from claseEmpleado import Empleado

class DePlanta(Empleado):
    __sueldoBasico = float()
    __antiguedad = int()
    
    def __init__(self, dni, nom, dire, tel, sbas, ant):
        super().__init__(dni, nom, dire, tel)
        self.__sueldoBasico = sbas
        self.__antiguedad = ant
        
    def calcularSueldo(self):
        porcentaje = (self.__sueldoBasico*self.__antiguedad)/100
        sueldo = self.__sueldoBasico * porcentaje
        return sueldo