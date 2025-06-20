from django.db import models
RAZA_CHOISE= [
	('Sin_Preferencia', 'Sin_Preferencia'),  
	('Bulldog_frances', 'Bulldog_frances'),
	('Bulldog', 'Bulldog'),
	('Pitbull_terrier', 'Pitbull_terrier'),
   	('Busterrier', 'Busterrier'),
	('Chihuahua', 'Chihuahua'),
	('Yorkshire', 'Yorkshire'),
	('Galgo', 'Galgo'),
	('Sharpei','Sharpei'),
	('Shitsu','Shitsu'),
	('Rottweiler','Rottweiler'),
	('Ovejero_aleman','Ovejero_aleman'),
	('Border_collie','Border_collie'),
	('Gran_danes','Gran_danes'),
	('Caniche','Caniche'),
	('Doberman','Doberman'),
	('Canecorso','Canecorso'),
	('San_Bernardo','San_Bernardo'),
	('Manto_Negro','Manto_Negro'),
	('Pequines','Pequines'),
	('Terranova','Terranova'),
	('Mestizo','Mestizo'),

]

EDAD_CHOISE=[
	('Sin Preferencia','Sin Preferencia'),
	('Junior','Junior'),
	('Adolesente','Adolesente'),
	('Mayor','Mayor'),
	('Señior','Señior'),
]
TAMAÑO_CHOISE = [
	('Sin Preferencia','Sin Preferencia'),
	('Pequeño','Pequeño'),
	('Mediano','Mediano'),
	('Grande','Grande'),
]



class Perro(models.Model):
	ESTADO_CHOICES = [
		('disponible','disponible'),
		('reservado','reservado'),
		('adoptado','adoptado'),
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
	nombre = models.CharField(max_length=100,default="Sin nombre")
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
