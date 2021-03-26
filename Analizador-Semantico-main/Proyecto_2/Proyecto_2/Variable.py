
class Variable:
    def __init__(self, tipo,nombre,valor,alcance,linea): #se definen los tipos de variables que analiza el analizador semantico#
        self.tipo = tipo   
        self.nombre = nombre #variable de tipo nombre
        self.alcance = alcance #variable de tipo alcance
        self.valor = valor #variable de tipo valor
        self.linea = linea #variable de tipo linea

    def getLinea(self):  
        return self.linea

    def getTipo(self):
        return self.tipo

    def getNombre(self):
        return self.nombre

    def getAlcance(self):
        return self.alcance
    
    def getValor(self):
        return self.valor

   
