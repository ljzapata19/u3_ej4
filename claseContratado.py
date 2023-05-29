from claseEmpleado import Empleado
class Contratado(Empleado):
    __fInicio = str()
    __fFin = str()
    __horas = int()
    __valorHora = float()
    
    def __init__(self, dni, nom, dire, tel, ini, fin, hor, val):
        super().__init__(dni, nom, dire, tel)
        self.__fInicio = ini
        self.__fFin = fin
        self.__horas = hor
        self.__valorHora = val
    
    def aumentarHoras(self, aumento):
        self.__horas += aumento        
    
    def imprimirContratado(self):
        super().imprimirEmpleado()
        print('Fecha de Inicio: ',self.__fInicio,'\nFecha de Finalización: ', self.__fFin,'\nHoras: ',self.__horas,'\nValor por Hora: ',self.__valorHora)
        

    def calcularSueldo(self):
        sueldo = self.__horas * self.__valorHora
        return sueldo