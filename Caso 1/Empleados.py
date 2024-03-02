from Fecha import Fecha

class Empleados:
    #aqui va el codigo
    '''---------------------------------
    # atributos
    ------------------------------------'''

    nombres=''
    apellidos=''
    '''---------------------------------
    # 1 = Masculino y 2 = femenino
    ------------------------------------'''
    sexo=0
    salario=0
    hijos=0

    '''-----------------------------------------
    # Asociaciones
    --------------------------------------------'''
     
    fechaNaciomiento = Fecha()
    fechaIngreso= Fecha()

    '''----------------------------------
    # Metodos 
    -------------------------------------'''

    # constructor

    def __init__(self, nombres, apellidos, salario, sexo, hijos):
        self.nombres=nombres
        self.apellidos=apellidos
        self.salario=salario
        self.sexo=sexo
        self.hijos=hijos

    def CambiarSalario(self, nSalario):
        #aqui va el codigo
        self.salario = nSalario
        return "el salario se ha actualizado a: "+ str(self.salario)
    
    def ConsultarSalario(self):
        #aqui va el codigo
        return self.salario
    
    def AumentoSalario(self):
        #aqui va el codigo
        aumento = self.salario*0.05
        nSalario = self.salario+aumento
        self.salario = nSalario
        return "su nuevo salario es: "+str(self.salario)
    
    def DuplicarSalario(self):
        # forma 1
        nuevoSalario=self.salario*2
        self.salario = nuevoSalario
        return self.salario
        # # forma 2
        # self.salario *= 2

    def SalarioAnual(self):
        salarioAnual=self.salario*12
        return "Su salario anual es "+str(salarioAnual)
        # #forma 2
        # return self.salario*12
    
    def ConsultarDiaCumpleanios(self):
        # aqui va el codigo 
        return self.fechaNaciomiento.ConsultarDia() 
    
    def ImpuestoAnual(self):
        # aqui va el codigo 
        return self.SalarioAnual()*0.195
        # #forma 2
        # return self.SalarioAnual()*0.195
    
    def CantidasHijos(self):
        # aqui va el codigo 
        return self.hijos
    
    def AuxilioEducativo(self):
        salarioAuxilio= self.salario*0.05
        auxilioEducativo= salarioAuxilio*self.hijos 
        return auxilioEducativo
    
    def AuxilioEducativo2(self, porcentaje):
        salarioAuxilio2= self.salario*porcentaje
        auxilioEducativo2= salarioAuxilio2*self.hijos 
        return auxilioEducativo2
    
    def DiferenciaSalarios(self, empleado2):
        diferencia= self.salario-empleado2
        return diferencia
