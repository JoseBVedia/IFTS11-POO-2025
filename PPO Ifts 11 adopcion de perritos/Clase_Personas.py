#Clase Personas
from Clase_Perro import Tamaño
from Clase_Perro import Raza
from Clase_Perro import Edad
from enum import Enum


class PersonasAdoptantes(object):

    def __init__(self,nombre,dni,email,preferencias_raza,preferencias_tamaño,preferencias_edad,historial_de_adopciones):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        if isinstance(preferencias_raza, Raza):
            self.preferencias_raza = preferencias_raza
        else:
            raise ValueError("El estado debe ser un miembro de la clase Tamaño")
        if isinstance(preferencias_tamaño, Tamaño):   #el chatgpt me recomendo poner esta funcion para que sea un valor valido a la hora de definir la variable
            self.preferencias_tamaño = preferencias_tamaño
        else:
            raise ValueError("El estado debe ser un miembro de la clase Tamaño")
        if isinstance(preferencias_edad, Edad):   #el chatgpt me recomendo poner esta funcion para que sea un valor valido a la hora de definir la variable
            self.preferencias_edad = preferencias_edad
        else:
            raise ValueError("El estado debe ser un miembro de la clase Tamaño")
        self.historial_de_adopciones = historial_de_adopciones
        pass

    def mostrar(self):
        print("nombre",self.nombre,"Dni:",self.dni, "correo:",self.email,"Raza preferencias: ",self.preferencias_raza.name,"edad de preferencia ",self.preferencias_edad.name, "tamaño referencia",self.preferencias_tamaño.name, "Hisotiral ",self.historial_de_adopciones,)

        return None

    def ver_historial(self):
        print("El historial es:",self.historial_de_adopciones,)
        return None
    
    def modificarDatos(self): #solo dejare modificar el mail y las preferencias ya que los otros datos son fijos y en caso del historia no se podra borrar
        print("Quiere modificar su mail")
        print("Coloque S para si o N para no ")
        condi = input()
        if condi == "S":
            self.email = input("Colocar su nuevo mail")
        print("Quiere modificar su Preferencias")
        print("Coloque S para si o N para no")
        condi = input()
        if condi == "S":
            self.preferencias_raza = input("Colocar su nueva raza ")
            self.preferencias_edad = input("Colocar su nueva edad ")
            self.preferencias_tamaño = input ("colocar el nuevo tamaño ")
        return None
    def ingresoPersona(self):
        nombre = input("ingrese Nombre ")
        self.nombre = nombre
        dni= input("ingrese dni ")
        self.dni = dni
        mail= input("ingrese mail ")
        self.email = mail
        self.preferencias_raza =input("raza de preferencia ")
        self.referencias_edad =input ("edad de prefe ")
        self.preferencias_tamaño = input("tamaño de prefe ")
        return None 


a = PersonasAdoptantes("carlos",3211111,"carlitos@hot",Raza.Bulldog_frances,Tamaño.Grande,Edad.Adulto,[1,2,3,4,5])
a.mostrar()


        


