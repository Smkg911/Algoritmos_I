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

    #constructor
    def __init__(self, valorInvertido, interesMensual, mesApertura):
        self.valorInvertido=valorInvertido
        self.interesMensual=interesMensual
        self.mesApertura=mesApertura

    def ValorInvertido(self):
        #aqui va el codigo
        return "su Valor Invertido actual es"+ self.valorInvertido
        
    def InteresMensual(self):
        #aqui va el codigo
        interes = self.valorInvertido*self.interesMensual
        nValorInvertido = self.valorInvertido+interes
        self.valorInvertido = nValorInvertido
        return self.valorInvertido
    
