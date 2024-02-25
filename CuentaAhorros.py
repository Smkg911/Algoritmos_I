class CuentaAhorros:
    #aqui va el codigo

    '''-----------------------
    #Atributos
    --------------------------'''
    saldo=0
    interesMensual=0

    '''---------------------------
    # Metodos 
    ------------------------------'''

    def ConsultarSaldo(self):
        #aqui va el codigo
        return "su salario actual es"+ self.saldo 
        
    def InteresMensual(self):
        #aqui va el codigo
        interes = self.saldo*0.006
        nSaldo = self.saldo+interes
        self.saldo = nSaldo
        return self.saldo

    def DepositarValor(self):
        #aqui va el codigo
        deposito = 0
        nSaldo = self.saldo+deposito
        self.saldo = nSaldo 
        
    def RetirarValor(self):
        #aqui va el codigo
        retiro = 0
        nSaldo = self.saldo-retiro 
        self.saldo = nSaldo 
