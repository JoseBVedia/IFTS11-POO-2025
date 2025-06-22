# Clase perro
from enum import Enum

class Edad(Enum):
    Sin_Preferencia = 0   # este lo pongo ahi para cuando haga personas adoptantes puedan elegir sin referencia
    Junior = 1
    Adolesente = 2
    Adulto = 3
    Señior = 4

class Raza(Enum):
    Sin_Preferencia = 0  # este lo pongo ahi para cuando haga personas adoptantes puedan elegir sin referencia
    Bulldog_frances = 1
    Bulldog = 2
    Pitbull_terrier = 3
    Busterrier = 4
    Chihuahua = 5
    Yorkshire = 6
    Galgo = 7
    Sharpei = 8
    Shitsu = 9
    Rottweiler = 10
    Ovejero_aleman = 11
    Border_collie = 12
    Gran_danes = 13
    Caniche = 14
    Doberman = 15
    Canecorso = 16
    San_Bernardo = 17
    Manto_Negro = 18
    Pequines = 19
    Terranova = 20
    Mestizo = 21



class Tamaño(Enum):
    Sin_Preferencia = 0
    Pequeño = 1
    Mediano = 2
    Grande = 3 

class Estado(Enum):  #se genera un enumerador para validar el estado del perro
    Disponible = 1
    Reservado = 2
    Adoptado = 3



class Perro(object):


    def __init__(self,id,nombre,raza,edad,tamaño,peso,vacunado,estado,temperamento,):
        self.id = id
        self.nombre = nombre
        if isinstance(raza, Raza):
            self.raza = raza
        else:
            raise ValueError("El estado debe ser un miembro de la clase edad")
        if isinstance(edad, Edad):
            self.edad = edad
        else:
            raise ValueError("El estado debe ser un miembro de la clase edad")
        if isinstance(tamaño, Tamaño):
            self.tamaño = tamaño
        else:
            raise ValueError("El estado debe ser un miembro de la clase Tamaño")
        self.peso = peso
        self.vacunado = vacunado
        if isinstance(estado, Estado):   #el chatgpt me recomendo poner esta funcion para que sea un valor valido a la hora de definir la variable
            self.estado = estado
        else:
            raise ValueError("El estado debe ser un miembro de la clase Estado")
        self.temperamento = temperamento
        pass

    def cambiar_estado(self):
        print("Coloque el nuevo estado del perro. Opciones:")
        for estado in Estado:
            print(f"- {estado.name}")
        nuevo_estado = input("Estado: ").capitalize()

        if nuevo_estado in Estado.__members__:
            self.estado = Estado[nuevo_estado]
            print(f"El estado ha sido cambiado a {self.estado.name}.")
        else:
            print("Estado inválido.")
    def mostrar(self):
        print("Nombre ",self.nombre,"Raza ",self.raza.name,"Edad ",self.edad.name,"Tamaño ",self.tamaño.name,"Peso",self.peso,"Estado ",self.estado.name,"Vacunado",self.vacunado,"Temperamento ",self.temperamento)
        return None
    def ingresarPerro(self):
        print("Ingrese los datos del perro:")
        self.id = int(input("ID: "))
        self.nombre = input("Nombre: ")
        print("\n Opciones de raza:")
        for raza in Raza:
            if raza != Raza.Sin_Preferencia:
                print(f"- {raza.name}")
        raza_input = input("Ingrese la raza (escriba exactamente como aparece): ").strip()
        if raza_input in Raza.__members__:
            self.raza = Raza[raza_input]
        else:
            raise ValueError("Raza inválida.")
        
        print("\n Opciones de edad:")
        for edad in Edad:
            if edad != Edad.Sin_Preferencia:
                print(f"- {edad.name}")
        edad_input = input("Ingrese la edad: ").strip()
        if edad_input in Edad.__members__:
            self.edad = Edad[edad_input]
        else:
            raise ValueError("Edad inválida.")
        
        print("\n Opciones de tamaño:")
        for tamaño in Tamaño:
            if tamaño != Tamaño.Sin_Preferencia:
                print(f"- {tamaño.name}")
        tamaño_input = input("Ingrese el tamaño: ").strip()
        if tamaño_input in Tamaño.__members__:
            self.tamaño = Tamaño[tamaño_input]
        else:
            raise ValueError("Tamaño inválido.")
        self.peso = float(input("Peso: "))
        self.vacunado = input("¿Está vacunado? (si/no): ").strip().lower() == "si"
        print("\n Opciones de estado:")
        for estado in Estado:
            print(f"- {estado.name}")
        estado_input = input("Ingrese el estado: ").strip().capitalize()
        if estado_input in Estado.__members__:
            self.estado = Estado[estado_input]
        else:
            raise ValueError("Estado inválido.")
        self.temperamento = input("Temperamento: ")
        return None

#a = Perro(1,"Pelusa",Raza.Bulldog_frances,Edad.Junior,Tamaño.Grande,14,"si",Estado.Disponible,"tranquilo")
#b =Perro(2,"mordelon",Raza.Mestizo,Edad.Adulto,Tamaño.Pequeño,14,"si",Estado.Reservado,"tranquilo")
#c = Perro(3,"pepin",Raza.Rottweiler,Edad.Señior,Tamaño.Pequeño,20,"si",Estado.Adoptado,"tranquilo")
#b.mostrar()
#a.mostrar()
#c.mostrar()

#b.cambiar_estado()
#b.mostrar()






