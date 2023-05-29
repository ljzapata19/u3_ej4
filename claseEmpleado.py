class Empleado:
    __dni = int()
    __nombre = str()
    __direccion = str()
    __telefono = str()
    
    def __init__(self, dni, nom, dire, tel):
        self.__dni = dni
        self.__nombre = nom
        self.__direccion = dire
        self.__telefono = tel
    
    def getDni(self):
        return self.__dni
    
    def imprimirEmpleado(self):
        print('Dni: ',self.__dni, '\nNombre: ',self.__nombre, '\nDireccion: ',self.__direccion,'\nTelefono: ',self.__telefono)
    
    def getNombre(self):
        return self.__nombre
    
    def getTelefono(self):
        return self.__telefono