class CDT:
    #aqui va el codigo

    '''--------------------------
    Atributos 
    -----------------------------'''
    valorInvertido=0
    interesMensual=0
    mesApertura=0

    '''---------------------------
    # Metodos 
    ------------------------------'''

    def ValorInvertido(self):
        #aqui va el codigo
        return "su Valor Invertido actual es"+ self.valorInvertido
        
    def InteresMensual(self):
        #aqui va el codigo
        interes = self.valorInvertido*0.1
        nValorInvertido = self.valorInvertido+interes
        self.valorInvertido = nValorInvertido
        return self.valorInvertido
