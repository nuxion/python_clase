
class CajaDeAhorro(type):

    descubierto = 500

    def __init__(self, saldo=0):
        self.saldo = saldo 

    def depositar(self, monto: int):
        self.saldo += monto 

    @classmethod
    def leer_descubierto(cls):
        print("El descubierto es de {}".format(cls.descubierto))
        
        #print("Descubierto")

    @classmethod
    def vip_client(cls):
        caja = cls(saldo=1000)
        return caja

    def leer_saldo(self):
        print(self.saldo)

    def get_self(self):
        return self

class ClienteIndividuo:

    def __init__(self, dni):
        self.dni = dni
        self.cuenta = CajaDeAhorro()

    def obtener_caja_ahorro(self):
        return self.cuenta

    def depositar(self, monto):
        self.cuenta.depositar(monto)

    def consultar_saldo(self):
        return self.cuenta.saldo

if __name__ == "__main__":
  
    cliente_vip = CajaDeAhorro.vip_client()
    print(type(cliente_vip))
    caja = CajaDeAhorro()
    caja.depositar(2500)
    print(caja.saldo)
    print(id(CajaDeAhorro))
    print(type(CajaDeAhorro))
    
    