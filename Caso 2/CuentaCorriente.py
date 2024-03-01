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
        self.saldo -= retiro
