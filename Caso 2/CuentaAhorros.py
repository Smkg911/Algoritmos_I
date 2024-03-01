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
    
    def ConsultarInteresMensual(self):
        #aqui va el codigo
        return self.interesMensual
        
    def InteresMensual(self):
        #aqui va el codigo
        interes = self.saldo*0.006
        nSaldo = self.saldo+interes
        self.saldo = nSaldo
        return self.saldo

    def DepositarValor(self, deposito):
        # aqui va el codigo
        self.saldo += deposito
        
    def RetirarValor(self, retiro):
        #aqui va el codigo
        self.saldo -= retiro
