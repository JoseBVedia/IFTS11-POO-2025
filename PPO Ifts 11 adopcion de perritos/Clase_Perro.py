# Clase perro
from enum import Enum

class Estado(Enum):  #se genera un enumerador para validar el estado del perro
    disponible = "Disponible"
    reservado = "Reservado"
    adoptado = "Adoptado"



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
        if isinstance(estado, Estado):   #el chatgpt me recomendo poner esta funcion para que sea un valor valido a la hora de definir la variable
            self.estado = estado
        else:
            raise ValueError("El estado debe ser un miembro de la clase Estado")
        self.temperamento = temperamento
        pass

    def cambiar_estado(self):
        print("Coloque el nuevo estado del perro (Disponible, Reservado, Adoptado):")
        nuevo_estado = input().lower()
        
        # Validamos el input y cambiamos el estado
        if nuevo_estado in Estado.__members__:  # Verificamos si el input es un estado válido
            self.estado = Estado[nuevo_estado]
            print(f"El estado ha sido cambiado a {self.estado.value}.")
        else:
            print("Estado inválido. Debe ser 'Disponible', 'Reservado' o 'Adoptado'.")
        return None
    
    def mostrar(self):
        print("El nombre es",self.nombre,"la raza es",self.raza,"su edad",self.edad,"su tamaño",self.tamaño,"su peso",self.peso,"estado de salud",self.estado_salud,"se encuentra",self.estado.value,"se encuentra vacunado",self.vacunado,"y su temperamento es",self.temperamento)
        return None

#a = Perro(1,"Pelusa","bulldog",6,"pequeño",14,"bueno","si",Estado.disponible,"tranquilo")
#b =Perro(2,"mordelon","mestizo",13,"pequeño",14,"regular","si",Estado.disponible,"tranquilo")
#c = Perro(3,"pepin","bulldog",20,"pequeño",20,"buneo","si",Estado.adoptado,"tranquilo")
#b.mostrar()
#a.mostrar()
#c.mostrar()

#b.cambiar_estado()
#b.mostrar()






