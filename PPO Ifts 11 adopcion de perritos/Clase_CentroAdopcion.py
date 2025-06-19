from Clase_Perro import Perro
from Clase_Perro import Estado
from Clase_Perro import Tamaño
from Clase_Perro import Raza
from Clase_Perro import Edad
from Clase_Personas import PersonasAdoptantes


class CentroAdopcion(object):
    def __init__(self,regPerros,regPersonas):
        self.regPerros = regPerros
        self.regPersonas = regPersonas
        pass 
    def ingresarperro(self,other):
        self.regPerros.append(other)
        return None
   
    def ingresarpersonas(self,other):
        self.regPersonas.append(other)
        return None
    
def matcher(self,usuario):
    i = 0
    while i < len(self):
        if self[i].estado.value == 1:
            if usuario.preferencias_raza == self[i].raza and usuario.preferencias_tamaño == self[i].tamaño and usuario.preferencias_edad == self[i].edad:  #La verdad profe queria seguir mejorando el match poniendo las opciones de que si no tiene preferencia le tire un listado pero estoy en pelotas con dganjo y prefiero mandarle a eso perdon
                print(self[i].id)
                usuario.historial_de_adopciones.append(self[i].id)
                self[i].cambiar_estado()
                return None
        i = i + 1
    print("no se encontro perro")
    return None

                



bdCentroAdopcion = CentroAdopcion([],[])
perro1 = Perro(1,"Raqueñ",Raza.Bulldog,Edad.Junior,Tamaño.Mediano,14,True,Estado.Disponible,"Tranquilo")
perro2 = Perro(2,"Pepin",Raza.Bulldog,Edad.Adulto,Tamaño.Mediano,14,True,Estado.Adoptado,"Tranquilo")
perro3 = Perro(3,"Pepin",Raza.Caniche,Edad.Junior,Tamaño.Pequeño,6,True,Estado.Disponible,"Tranquilo")
perro4 = Perro(1,"Raquel",Raza.Bulldog,Edad.Junior,Tamaño.Grande,14,True,Estado.Disponible,"Tranquilo")
perro5 = Perro(1,"Chuchi",Raza.Rottweiler,Edad.Junior,Tamaño.Mediano,18,True,Estado.Disponible,"Tranquilo")
bdCentroAdopcion.ingresarperro(perro1)
bdCentroAdopcion.ingresarperro(perro2)
bdCentroAdopcion.ingresarperro(perro3)
bdCentroAdopcion.ingresarperro(perro4)
bdCentroAdopcion.ingresarperro(perro5)
persona1 = PersonasAdoptantes("CARLOS",3333,"CarlosReloco@hotmail.com",Raza.Bulldog,Tamaño.Mediano,Edad.Junior,[])
persona2 = PersonasAdoptantes("Michel",3215,"Michel69@gmail.com",Raza.Rottweiler,Tamaño.Grande,Edad.Junior,[])
bdCentroAdopcion.ingresarpersonas(persona1)
bdCentroAdopcion.ingresarpersonas(persona2)
print(len(bdCentroAdopcion.regPerros))
bdCentroAdopcion.regPerros[0].mostrar()
matcher(bdCentroAdopcion.regPerros,bdCentroAdopcion.regPersonas[0])
bdCentroAdopcion.regPersonas[0].ver_historial()
bdCentroAdopcion.regPersonas[1].modificar_datos()




#c = Perro(3,"Cesar","mestizo",11,"mediano",18,"bueno","si",Estado.adoptado,"Jugueton")
##a.mostrar()
#bdPerros.ingresarperro(a)
#bdPerros.ingresarperro(b)
#bdPerros.ingresarperro(c)
#a1 = bdPerros.regPerros[0]
#b2 = bdPerros.regPerros[1]
#c2 = bdPerros.regPerros[2]
#a1.mostrar()
#b2.mostrar()
#c2.mostrar()
#a1.cambiar_estado()
#a1.mostrar()
