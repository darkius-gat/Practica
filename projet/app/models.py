from django.db import models

# Create your models here.


class Carrera(models.Model):
	titulo = models.CharField(max_length=140)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.titulo


class Alumno(models.Model):
	alumno = models.CharField(max_length=140)
	imagen = models.ImageField(upload_to="articulos/")
	carrera = models.ForeignKey(Carrera)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s - %s" %(self.titulo, self.autor)