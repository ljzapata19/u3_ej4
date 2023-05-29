from claseManejadorEmpleados import ManejadorEmpleados

if __name__ == '__main__':
    
    #Definir una clase colección basada en un arreglo Numpy, cuyo tamaño se debe
    #ingresar por teclado, para almacenar los empleados de la empresa
    cant_empleados = int(input('Ingrese la cantidad de empleados: '))
    empleados = ManejadorEmpleados(cant_empleados)
    
    #Almacenar en memoria principal los empleados de la empresa
    #cargar empleados de la planta
    empleados.testEmpleados()
    
    #Ingresar el DNI de un empleado y la cantidad de horas trabajadas
    #en el día de la fecha e incrementar la cantidad de las horas trabajadas del empleado
    print('\n\n1.   Registrar horas')
    empleados.registrarHoras()
    
    #Dada una tarea mostrar el monto a pagar para ella. Solo se
    #consideran las tareas que no han finalizado
    print('\n\n2.   Total de tarea')
    empleados.totalDeTarea()
    
    #La empresa dará una ayuda solidaria a los empleados cuyo
    #sueldo sea inferior a $150000; listar nombre, dirección y DNI de los empleados que les
    #corresponde la ayuda
    print('\n\n3.   Ayuda Económica.')
    empleados.ayudaEconomica()
    
    #Mostrar nombre, teléfono y sueldo a cobrar de todos los
    #empleados
    print('\n\n4.   Calcular sueldo:')
    empleados.calcularSueldos()