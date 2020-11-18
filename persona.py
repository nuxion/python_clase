
mi_variable = "Hola mundo"

class Persona:

    def __init__(self, nombre, apellido, es_presidente=False):
        self.nombre = nombre
        self.apellido = apellido
        self.es_presidente = es_presidente

    def saludar(self):
        if self.es_presidente:
            print("Hola soy el presidente {} {}".format(self.nombre, self.apellido))
        else:
            print("Hola soy {} {}".format(self.nombre, self.apellido))
 

if __name__ == "__main__":
    print("Mi programa")
    print(mi_variable)
    pepe = Persona("Pepe", "Mujica", es_presidente=True)
    alberto = Persona("Alberto", "Fernandez", es_presidente=True)
    pepe.saludar()
    alberto.saludar()
    juan = Persona("Juan", "Garay")
    juan.saludar()

    