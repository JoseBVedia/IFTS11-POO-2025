# Clase perro
from enum import Enum

class Estado(Enum):  #se genera un enumerador para validar el estado del perro
    disponible = 1
    reservado = 2
    adoptado = 3



class Perro(object):


    def __init__(self,id,nombre,raza,edad,tamaño,peso,estado_salud,vacunado,estado,temperamento,):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado
        self.temperamento = temperamento
        pass

    def cambiar_estado(self):
        print("Coloque 1 si el perro vuelve a estar disponible, coloque 2 si el perro se encuentra reservado o 3 si el perro fue adoptado")
        self.estado = input()
        return None
    
    def mostrar(self):
        print("El nombre es",self.nombre,"la raza es",self.raza,"su edad",self.edad,"su tamaño",self.tamaño,"su peso",self.peso,"estado de salud",self.estado_salud,"se encuentra",self.estado,"se encuentra vacunado",self.vacunado,"y su temperamento es",self.temperamento)
        return None

a = Perro(1,"Pelusa","bulldog",6,"pequeño",14,"bueno","si",1,"tranquilo")
b =Perro(2,"mordelon","mestizo",13,"pequeño",14,"regular","si",2,"tranquilo")
b.mostrar()
a.mostrar()

b.cambiar_estado()
b.mostrar()






