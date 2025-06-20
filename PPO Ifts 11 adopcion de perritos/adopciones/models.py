from django.db import models
RAZA_CHOISE= [
	(0, 'Sin_Preferencia'),  
	(1, 'Bulldog_frances'),
	(2, 'Bulldog'),
	(3, 'Pitbull_terrier'),
   	(4, 'Busterrier'),
	(5, 'Chihuahua'),
	(6, 'Yorkshire'),
	(7, 'Galgo'),
	(8,'Sharpei'),
	(9,'Shitsu'),
	(10,'Rottweiler'),
	(11,'Ovejero_aleman'),
	(12,'Border_collie'),
	(13,'Gran_danes'),
	(14,'Caniche'),
	(15,'Doberman'),
	(16,'Canecorso'),
	(17,'San_Bernardo'),
	(18,'Manto_Negro'),
	(19,'Pequines'),
	(20,'Terranova'),
	(21,'Mestizo'),

]

EDAD_CHOISE=[
	(0,'Sin Preferencia'),
	(1,'Junior'),
	(2,'Adolesente'),
	(3,'Mayor'),
	(4,'Señior'),
]
TAMAÑO_CHOISE = [
	(0,'Sin Preferencia'),
	(1,'Pequeño'),
	(2,'Mediano'),
	(3,'Grande'),
]



class Perro(models.Model):
	ESTADO_CHOICES = [
		(1,'disponible'),
		(2,'reservado'),
		(3,'adoptado'),
    	]
	nombre = models.CharField(max_length=100)
	raza = models.CharField(max_length=40, choices=RAZA_CHOISE, default='Mestizo')
	edad = models.CharField(max_length=20, choices=EDAD_CHOISE, default='Junior')
	tamaño = models.CharField(max_length=20, choices=TAMAÑO_CHOISE, default='Pequeño')
	peso = models.DecimalField(max_digits=5, decimal_places=2)
	vacunado = models.BooleanField(default=False)
	estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
	temperamento = models.CharField(max_length=100)

def __str__(self):
    return f"{self.nombre} ({self.raza})"

class PersonasAdoptantes(models.Model):
	user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
	dni = models.CharField(max_length=20, unique=True)
	telefono = models.CharField(max_length=20)
	direccion = models.TextField()
	preferencias_raza = models.CharField(max_length=40, choices=RAZA_CHOISE, default='Sin_Preferencia')
	preferencias_edad = models.CharField(max_length=20, choices=EDAD_CHOISE, default='Junior')
	preferencias_tamaño = models.CharField(max_length=20, choices=TAMAÑO_CHOISE, default='Pequeño')
def __str__(self):
    return self.user.get_full_name() or self.user.username

class Adopcion(models.Model):
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(PersonasAdoptantes, on_delete=models.CASCADE)
    fecha_adopcion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
def __str__(self):
    return f"Adopción de {self.perro} por {self.usuario}"
# Create your models here.
