class CuentaCorriente:
    #aqui va el codigo

    '''--------------------------
    #Atributos 
    -----------------------------'''
    saldo1=0

    '''---------------------------
    # Metodos 
    ------------------------------'''

    def ConsultarSaldo(self):
        #aqui va el codigo
        return "su salario actual es"+ self.saldo
    
    def DepositarValor(self, deposito):
        #aqui va el codigo
        deposito = 0
        nSaldo = self.saldo+deposito
        self.saldo = nSaldo 
        return "Usted ha depositado"+deposito
    
    def RetirarValor(self, retiro):
        #aqui va el codigo
        retiro = 0
        nSaldo = self.saldo-retiro 
        self.saldo = nSaldo 
        if retiro <= self.saldo:
            self.saldo < retiro
            return "usted ha retirado"+ retiro
        else:
            return "fondos insuficientes"