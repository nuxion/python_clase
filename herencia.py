

class VehiculoTerrestre:

    PADRE = "Mi variable estatica"

    def __init__(self):
        self.altura = 10
        self.ancho = 20
        self.largo = 30
        print("Utilizando constructor padre")

    def encender(self):
        print("Encendido, desde Padre") 

    def print_padre(self):
        print(self.PADRE)

class Autobus(VehiculoTerrestre):

    def __init__(self, altura, ancho, largo, capacidad):
        #super().__init__()
        self.capacidad = capacidad
        self.padre = False
        self.altura = 10
        self.ancho = 20
        self.largo = 30

    def print_datos(self):
        print("Ancho: {}, Largo: {}, capacidad: {}".format(self.ancho, self.largo, self.capacidad))
       
    def encender(self, msg):
        print("Encendido desde Hijo. {}".format(msg))

if __name__ == "__main__":
    vt = VehiculoTerrestre()
    vt.encender()
    vt.print_padre()
    a = Autobus(10, 30, 50)
    a = Autobus(55, 20, 30, 10)
    a.print_datos()
    a.encender("Saludos.")
    a.print_padre()
