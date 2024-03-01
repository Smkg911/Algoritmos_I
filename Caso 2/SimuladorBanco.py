from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

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

    ahorros= CuentaAhorros()
    corriente= CuentaCorriente() 
    cdt = CDT()

    '''----------------------------------------------------
    # metodos 
    --------------------------------------------------------'''
    #constructor

    def __init__(self, cedula, nombre, mesActual):
        self.cedula=cedula
        self.nombre=nombre
        self.mesActual=mesActual

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
        saldoAhorros= self.ahorros.ConsultarSaldo()
        self.ahorros.RetirarValor(saldoAhorros)
        self.corriente.DepositarValor(saldoAhorros)
        return saldoAhorros
        # forma 2
        #self.ConsignarCuentaCorriente(self.ahorros.ConsultarSaldo())
        #self.ahorros.RetirarValor(self.ahorros.ConsultarSaldo())
    
    def DuplicarSaldoAhorros(self):
        # aqui va el codigo
        return self.ahorros.ConsultarSaldo()*2
        # forma 2
        #self.ahorros.ConsignarCuentaAhorros(self.ahorros.ConsultarSaldo())
    
    def RetirarAhorro(self, retiro):
        #aqui va el codigo
        return self.corriente.RetirarValor(retiro)
    
    def ConsultarSaldoCorriente(self):
        # aqui va el codigo
        return "su saldo en la cuenta corriente es"+ self.corriente.ConsultarSaldo()
    
    def RetirarTodo(self):
        # aqui va el codigo
        saldoAhorros= self.ahorros.ConsultarSaldo()
        saldoCorriente= self.corriente.ConsultarSaldo()
        retiro=saldoAhorros+saldoCorriente
        self.ahorros.RetirarValor(saldoAhorros)
        self.corriente.RetirarValor(saldoCorriente)
        return retiro
