from claseEmpleado import Empleado
class Externo(Empleado):
    __tarea = str()
    __fInicio = str()
    __fFin = str()
    __viatico = float()
    __costoObra = float()
    __seguro = float()
    
    def __init__(self, dni, nom, dire, tel, tar, ini, fin, viat, co, seg):
        super().__init__(dni, nom, dire, tel)
        self.__tarea = tar
        self.__fInicio = ini
        self.__fFin = fin
        self.__viatico = viat
        self.__costoObra = co
        self.__seguro = seg
        
    def getTarea(self):
        return self.__tarea
    
    def getViatico(self):
        return self.__viatico
    
    def getCostoObra(self):
        return self.__costoObra
    
    def getSeguro(self):
        return self.__seguro
    
    def getFechaFin(self):
        return self.__fFin
    
    def imprimirExterno(self):
        super().imprimirEmpleado()
        print('Tarea: ',self.__tarea,'Fecha de Inicio: ',self.__fInicio,'\nFecha de Finalización: ', self.__fFin,'\nMonto Viatico: ',self.__viatico,'\nCosto de Obra: ',self.__costoObra,'\nMonto Seguro: ',self.__seguro)
    
    def calcularSueldo(self):
        return self.__costoObra - self.__viatico - self.__seguro