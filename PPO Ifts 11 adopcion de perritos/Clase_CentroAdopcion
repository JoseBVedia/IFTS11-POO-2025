from Clase_Perro import Perro
from Clase_Perro import Estado
from Clase_Personas import PersonasAdoptantes
from Clase_Personas import Preferencias


class CentroAdopcion(object):
    def __init__(self,regPerros,regPersonas):
        self.regPerros = regPerros
        self.regPersonas = regPersonas
        pass 
    def ingresarperro(self,other):
        self.regPerros.append(other)
        return None
   
    def ingresarpersonas(self,other):
        self.append(other)
        return None


bdPerros = CentroAdopcion([],[])
a = Perro(1,"pepin","pitbull",3,"pequeño",15,"correcto","si",Estado.disponible,"tranquilo")
b = Perro(2,"carlos","Salchicha",12,"pequeño",5,"bueno","si",Estado.reservado,"no se lleva bien con otros perro")
c = Perro(3,"Cesar","mestizo",11,"mediano",18,"bueno","si",Estado.adoptado,"Jugueton")
#a.mostrar()
bdPerros.ingresarperro(a)
bdPerros.ingresarperro(b)
bdPerros.ingresarperro(c)
a1 = bdPerros.regPerros[0]
b2 = bdPerros.regPerros[1]
c2 = bdPerros.regPerros[2]
a1.mostrar()
b2.mostrar()
c2.mostrar()
a1.cambiar_estado()
a1.mostrar()
