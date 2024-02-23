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