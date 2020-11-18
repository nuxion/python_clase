

class Saludo:

    def __init__(self):
        pass

    def saludo(self, mensaje="hola mundo"):
        print(mensaje)
        
          
if __name__ == "__main__":
    saludo = Saludo()
    # hola mundo   
    saludo.saludo()
    # chau mundo
    saludo.saludo(mensaje="Chau mundo")

    
    
    