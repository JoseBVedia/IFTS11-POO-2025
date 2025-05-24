#Clase Personas

class Preferencias(object):
    def __init__(self,raza,tamaño,edad):
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        pass

class PersonasAdoptantes(object):

    def __init__(self,nombre,dni,email,preferencias,historial_de_adopciones):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias
        self.historial_de_adopciones = historial_de_adopciones
        pass

    def mostrar(self):
        print("El nombre del adoptante es ",self.nombre,"su Dni es ",self.dni, "su direccion de correo es ",self.email,"este en buscar de un ",self.preferencias.raza,"de una edad aproximada de ",self.preferencias.edad, "y de tamaño ",self.preferencias.tamaño, "y a adoptado una cantidad de ",self.historial_de_adopciones,)
        #print(self.nombre)
        #print(self.dni)
        #print(self.email)
        #print(self.preferencias.raza,self.preferencias.edad,self.preferencias.tamaño)
        #print(self.historial_de_adopciones)
        return None

    def ver_historial(self):
        print("El historial es:",self.historial_de_adopciones,)
        return None
    
    def modificarDatos(self): #solo dejare modificar el mail y las preferencias ya que los otros datos son fijos y en caso del historia no se podra borrar
        print("Quiere modificar su mail")
        print("Coloque S para si o N para no")
        condi = input()
        if condi == "S":
            self.email = input("Colocar su nuevo mail")
        print("Quiere modificar su Preferencias")
        print("Coloque S para si o N para no")
        condi = input()
        if condi == "S":
            self.preferencias.raza = input("Colocar su nueva raza")
            self.preferencias.edad = input("Colocar su nueva edad")
            self.preferencias.tamaño = input ("colocar el nuevo tamaño")
        return None
    def ingresoPersona(self):
        nombre = input("ingrese Nombre")
        self.nombre = nombre
        dni= input("ingrese dni")
        self.dni = dni
        mail= input("ingrese mail")
        self.email = mail
        razaPrefe =input("raza de preferencia")
        edadPrefe =input ("edad de prefe")
        tamañoPrefe = input("tamaño de prefe")
        Prefeingreso = Preferencias(razaPrefe,tamañoPrefe,edadPrefe)
        self.preferencias = Prefeingreso
        return None 


#aprefe = Preferencias("bulldog","pequeño",5)
#a = PersonasAdoptantes("carlos",3211111,"carlitos@hot",aprefe,[1,2,3,4])
#a.mostrar()
#a.modificarDatos()
#a.mostrar()
#d = PersonasAdoptantes(0,0,0,"0",0) #primero defino un numero de usuario en este caso d y digo que va hacer una persona de Tipo clase adoptantes
#d.ingresoPersona()
#d.mostrar()


        


