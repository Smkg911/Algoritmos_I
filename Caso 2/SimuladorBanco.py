from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    #aqui va el codigo

    '''-------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------'''
    cedula=0
    nombre=''
    mesActual=0
    '''-----------------------------------------------------------------------
    # 1 = Vip y 2 = Platino y 3 = Normal 
    -------------------------------------------------------------------------'''
    cliente=0


    '''------------------------------------------------------------------------
    # Asociaciones
    ---------------------------------------------------------------------------'''

    ahorros= CuentaAhorros()
    corriente= CuentaCorriente() 
    cdt = CDT()

    '''-----------------------------------------------------------------------------------
    # metodos 
    ------------------------------------------------------------------------------------'''
    #constructor

    def __init__(self, cedula, nombre, mesActual, cliente):
        self.cedula=cedula
        self.nombre=nombre
        self.mesActual=mesActual
        self.cliente=cliente

    def ConsultarSaldoTotal (self):
        #aqui va el codigo
        return "su saldo total es"+ self.ahorros.ConsultarSaldo()+ self.corriente.ConsultarSaldo()
        
    def ConsignarCuentaCorriente(self, deposito):
        #aqui va el codigo 
        return self.corriente.DepositarValor(deposito)
    
    def ConsignarCuentaAhorros(self, deposito):
    #aqui va el codigo 
        return self.ahorros.DepositarValor(deposito)
    def CuentaAhorrosCorriente(self):
        #aqui va el codigo
        self.ConsignarCuentaCorriente(self.ahorros.ConsultarSaldo())
        self.ahorros.RetirarValor(self.ahorros.ConsultarSaldo())

        # forma 2
        # saldoAhorros= self.ahorros.ConsultarSaldo()
        # self.ahorros.RetirarValor(saldoAhorros)
        # self.corriente.DepositarValor(saldoAhorros)
        # return saldoAhorros
    
    def DuplicarSaldoAhorros(self):
        # aqui va el codigo
        self.ahorros.ConsignarCuentaAhorros(self.ahorros.ConsultarSaldo())
        # forma 2
        # return self.ahorros.ConsultarSaldo()*2
    
    def RetirarAhorro(self, retiro):
        #aqui va el codigo
        return self.corriente.RetirarValor(retiro)
    
    def ConsultarSaldoCorriente(self):
        # aqui va el codigo
        return "su saldo en la cuenta corriente es"+ self.corriente.ConsultarSaldo()

    def RetirarTodo(self):
        # aqui va el codigo
        total = self.CalcularSaldoToTal()
        self.TransferirAhorrosACorriente()
        self.RetirarCuentaCorriente(total)
        return total 
        # forma 2
        # saldoAhorros= self.ahorros.ConsultarSaldo()
        # saldoCorriente= self.corriente.ConsultarSaldo()
        # retiro=saldoAhorros+saldoCorriente
        # self.ahorros.RetirarValor(saldoAhorros)
        # self.corriente.RetirarValor(saldoCorriente)
        # return retiro

    
    def cambiarTipoCliente(self, nuevoTipoCliente):
        self.cliente=nuevoTipoCliente
