from Fecha import Fecha

class empleado:
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

    '''-----------------------------------------
    # Asociaciones
    --------------------------------------------'''
     
    fechaNaciomiento = Fecha()
    fechaIngreso= Fecha()

    '''----------------------------------
    # Metodos 
    -------------------------------------'''

    def CambiarSalario(self, nSalario):
        #aqui va el codigo
        self.salario = nSalario
        return "el salario se ha actualizado a: "+ self.salario 
    
    def ConsultarSalario(self):
        #aqui va el codigo
        return self.salario
    
    def AumentoSalario(self):
        #aqui va el codigo
        aumento = self.salario*0.05
        nSalario = self.salario+aumento
        self.salario = nSalario
        return "su nuevo salario es: "+ self.salario
    
    def DuplicarSalario(self):
        # forma 1
        nuevoSalario=self.salario*2
        self.salario = nuevoSalario
        # # forma 2
        # self.salario *= 2

    def SalarioAnual(self):
        salarioAnual=self.salario*12
        return "Su salario anual es"+salarioAnual
        # #forma 2
        # return self.salario*12
    
    def ConsultarDiaCumpleanios(self):
        # aqui va el codigo 
        return self.fechaNaciomiento.ConsultarDia() 
    
    def ImpuestoAnual(self):
        # aqui va el codigo 
        impuesto = self.SalarioAnual()*0.195
        return "su impuesto anual sera de"+impuesto
        # #forma 2
        # return self.SalarioAnual()*0.195
    
    
