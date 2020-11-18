from datetime import datetime

class Perro:

    def __init__(self, estado, nombre, fecha, peso):
        self.nombre = nombre
        self.fecha = fecha
        self.peso = peso
        self.publicado = False

    def publicar(self):
        self.publicado = True

    def adoptar(self, msg):
        self.estado = msg

def publicar(mi_mascota):
    mi_mascota.publicar()


firulais = Mascota(estado="En Adopcion",nombre="Firulais",fecha=datetime.now(),peso="4kg")
firulais.cambiar_el_nombre("pepe")
print(firulais.nombre)
firulais.nombre = "Bola de nieve IV"
print(firulais.nombre)
