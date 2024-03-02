class CuentaCorriente:
    #aqui va el codigo

    '''--------------------------
    #Atributos 
    -----------------------------'''
    saldo=0

    '''---------------------------
    # Metodos 
    ------------------------------'''
    #constructor
    def __init__(self, saldo):
        self.saldo=saldo

    def ConsultarSaldo(self):
        #aqui va el codigo
        return "su salario actual es"+ self.saldo
    
    def DepositarValor(self, deposito):
        #aqui va el codigo
        self.saldo += deposito 
    
    def RetirarValor(self, retiro):
        #aqui va el codigo
        valorRetirado=retiro*0.01
        nsaldo=self.saldo-(valorRetirado+retiro)
        self.saldo=nsaldo
        return "usted ha retirado "+retiro
        
