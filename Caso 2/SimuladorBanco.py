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
        saldoAhorros= self.CuentaAhorros.ConsultarSaldo()
        self.CuentaAhorros.RetirarValor(saldoAhorros)
        self.CuentaCorriente.DepositarValor(saldoAhorros)
        return "usted ha retirado"+saldoAhorros
    
    def DuplicarSaldoAhorros(self):
        nuevoSaldo= self.CuentaAhorros.saldo()*2
        self.CuentaAhorros.saldo()=nuevoSaldo 
