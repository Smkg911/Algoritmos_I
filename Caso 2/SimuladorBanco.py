from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente

class SimuladorBancario:
    #aqui va el codigo

    '''-----------------------------------
    # Atributos
    -------------------------------------'''
    cedula=0
    nombre=''
    mesActual=0
    '''-----------------------------------------
    # Asociaciones
    --------------------------------------------'''

    saldoAhorros= CuentaAhorros()
    saldoCorriente= CuentaCorriente() 

    def ConsultarSaldoTotal (self):
        #aqui va el codigo
        return "su saldo total es"+ self.CuentaCorriente.saldoCorriente()+ self.CuentaAhorros.saldoAhorros()
    
    def ConsignarCuentaCorriente(self, deposito):
        #aqui va el codigo 
        return self.CuentaCorriente.DepositarValor(deposito)
    
    def CuentaAhorrosCorriente(self):
        #aqui va el codigo
        saldoAhorros= self.CuentaAhorros.ConsultarSaldo()
        self.CuentaAhorros.RetirarValor(saldoAhorros)
        self.CuentaCorriente.DepositarValor(saldoAhorros)
        return "usted ha retirado"+saldoAhorros
    
    def DuplicarSaldoAhorros(self):
        # aqui va el codigo
        nuevoSaldo= self.CuentaAhorros.saldo()*2
        self.CuentaAhorros.saldo=nuevoSaldo 
        return "su saldo se ha duplicado a"+ nuevoSaldo
    
    def RetirarAhorro(self, retiro):
        #aqui va el codigo
        return self.CuentaCorriente.RetirarValor(retiro)
    
    def ConsultarSaldoCorriente(self):
        # aqui va el codigo
        return "su saldo en la cuenta corriente es"+ self.CuentaCorriente.ConsultarSaldo()
    
    def RetirarTodo(self,):
        # aqui va el codigo
        saldoAhorros= self.CuentaAhorros.ConsultarSaldo()
        saldoCorriente= self.CuentaCorriente.ConsultarSaldo()
        retiro=saldoAhorros+saldoCorriente
        self.CuentaAhorros.RetirarValor(saldoAhorros)
        self.CuentaCorriente.RetirarValor(saldoCorriente)
        return "usted ha retirado un total de"+retiro
