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
    
    def modificar_datos(self):
        print("\n--- Modificación de Datos ---")
        respuesta = input("¿Desea modificar su email? (S/N): ").strip().upper()
        if respuesta == "S":
            nuevo_email = input("Ingrese su nuevo email: ").strip()
            self.email = nuevo_email
        respuesta = input("¿Desea modificar sus preferencias? (S/N): ").strip().upper()
        if respuesta == "S":
            print("\nOpciones de raza:")
            for raza in Raza:
                if raza != Raza.Todos:
                    print(f"- {raza.name}")
            nueva_raza = input("Ingrese nueva raza (escriba exactamente como aparece): ").strip()
            if nueva_raza in Raza.__members__:
                self.preferencias_raza = Raza[nueva_raza]
            else:
                print("Raza inválida. No se cambió.")

            print("\nOpciones de edad:")
            for edad in Edad:
                if edad != Edad.Todos:
                    print(f"- {edad.name}")
            nueva_edad = input("Ingrese nueva edad: ").strip()
            if nueva_edad in Edad.__members__:
                self.preferencias_edad = Edad[nueva_edad]
            else:
                print("Edad inválida. No se cambió.")

            print("\nOpciones de tamaño:")
            for tam in Tamaño:
                print(f"- {tam.name}")
            nuevo_tamaño = input("Ingrese nuevo tamaño: ").strip()
            if nuevo_tamaño in Tamaño.__members__:
                self.preferencias_tamaño = Tamaño[nuevo_tamaño]
            else:
                print("Tamaño inválido. No se cambió.")

            print("\nDatos actualizados correctamente.")
    
    def ingresoPersona(self):
        nombre = input("ingrese Nombre ")
        self.nombre = nombre
        dni= input("ingrese dni ")
        self.dni = dni
        mail= input("ingrese mail ")
        self.email = mail
        self.preferencias_raza =input("raza de preferencia ")
        self.preferencias_edad =input ("edad de prefe ")
        self.preferencias_tamaño = input("tamaño de prefe ")
        return None 


#a = PersonasAdoptantes("carlos",3211111,"carlitos@hot",Raza.Bulldog_frances,Tamaño.Grande,Edad.Adulto,[1,2,3,4,5])
#a.mostrar()


        


