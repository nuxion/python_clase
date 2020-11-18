
class Rueda:

    def __init__(self, id):
        self._id = id
    
    def get_id(self):
        return self._id


class Motor:

    def __init__(self, peso, cilindrada):
        self.peso = peso 
        self.cilindrada = cilindrada

    def get_cilindrada(self):
        return self.cilindrada

    def set_cilindrada(self, cilindrada):
        self.cilindrada = cilindrada

class Auto:

    def __init__(self, color, motor, ruedas):
        self.color = color
        self.motor = motor
        self.ruedas = ruedas
        
    def print_ruedas(self):
        for r in self.ruedas:
            print("Type r: ", type(r))
            print(r._id)

    def acelerar(self, velocidad=10, nitro=None):
        if nitro:
            velocidad += 20
        print("Acelera a {} km/h".format(velocidad))
    
    def encender(self):
        pass
    
    def frenar(self):
        pass

    def get_motor(self):
        return self.motor.get_cilindrada()


if __name__ == '__main__':

    v8 = Motor("250k", cilindrada="tete")
    
    ruedas = list()
    ruedas.append(Rueda(id=1))
    ruedas.append(Rueda(id=2))
    ruedas.append(Rueda(id=3))
    mi_auto = Auto(color="rojo", motor=v8, ruedas=ruedas)
    mi_auto.print_ruedas()