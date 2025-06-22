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
        print("\n Modificación de Datos ")
        respuesta = input("¿Desea modificar su email? (S/N): ").strip().upper()
        if respuesta == "S":
            nuevo_email = input("Ingrese su nuevo email: ").strip()
            self.email = nuevo_email
        respuesta = input("¿Desea modificar sus preferencias? (S/N): ").strip().upper()
        if respuesta == "S":
            print("\n Opciones de raza:")
            for raza in Raza:
                print(f"- {raza.name}")
            nueva_raza = input("Ingrese nueva raza (escriba exactamente como aparece): ").strip()
            if nueva_raza in Raza.__members__:
                self.preferencias_raza = Raza[nueva_raza]
            else:
                print("Raza inválida. No se cambió.")
            print("\n Opciones de edad:")
            for edad in Edad:
                print(f"- {edad.name}")
            nueva_edad = input("Ingrese nueva edad: ").strip()
            if nueva_edad in Edad.__members__:
                self.preferencias_edad = Edad[nueva_edad]
            else:
                print("Edad inválida. No se cambió.")
            print("\n Opciones de tamaño:")
            for tamaño in Tamaño:
                print(f"- {tamaño.name}")
            nuevo_tamaño = input("Ingrese nuevo tamaño: ").strip()
            if nuevo_tamaño in Tamaño.__members__:
                self.preferencias_tamaño = Tamaño[nuevo_tamaño]
            else:
                print("Tamaño inválido. No se cambió.")

            print("\nDatos actualizados correctamente.")
    
    def ingresoPersona(self):
        nombre = input("Ingrese su nombre: ")
        self.nombre = nombre
        dni = int(input("Ingrese su DNI: "))
        self.dni = dni
        email = input("Ingrese su correo electrónico: ")
        self.email = email
        print("\n Opciones de raza:")
        for raza in Raza:
            print(f"- {raza.name}")
        preferencias_raza = input("Ingrese su raza preferida (escriba exactamente como aparece): ").strip()
        if preferencias_raza in Raza.__members__:
            preferencias_raza = Raza[preferencias_raza]
        else:
            print("Raza inválida. Se establecerá como Sin Preferencia.") 
            preferencias_raza = Raza.Sin_Preferencia
        print("\n Opciones de edad:")
        for edad in Edad:
            print(f"- {edad.name}")
        preferencias_edad = input("Ingrese su edad preferida: ").strip()
        if preferencias_edad in Edad.__members__:
            preferencias_edad = Edad[preferencias_edad]
        else:
            print("Edad inválida. Se establecerá como Sin Preferencia.") 
            preferencias_edad = Edad.Sin_Preferencia
        print("\n Opciones de tamaño:")
        for tamaño in Tamaño:
            print(f"- {tamaño.name}")
        preferencias_tamaño = input("Ingrese su tamaño preferido: ").strip()
        if preferencias_tamaño in Tamaño.__members__:
            preferencias_tamaño = Tamaño[preferencias_tamaño]
        else:
            print("Tamaño inválido. Se establecerá como Sin Preferencia.") 
            preferencias_tamaño = Tamaño.Sin_Preferencia
        return None 


#a = PersonasAdoptantes("carlos",3211111,"carlitos@hot",Raza.Bulldog_frances,Tamaño.Grande,Edad.Adulto,[1,2,3,4,5])
#a.mostrar()


        


