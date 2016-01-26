from django.db import models


class Alumno(models.Model):
	TIPO = (
		('PG','Publico en General'),
		('AP','Alumno IPN'),
		('EP','Empleado IPN'),
		
	)
	nombre = models.CharField(max_length=64)
	apellido_paterno = models.CharField(max_length=64)
	apellido_materno = models.CharField(max_length=64)
	tipo = models.CharField(max_length=2,choices=TIPO)
	correo_electronico = models.EmailField(max_length=75)	
	cursos_inscritos = models.ManyToManyField('Curso', blank= True,null=True, related_name='cursos')
	def cursos_inscritos_anteriormente(self):
                cursos =  self.cursos_inscritos.all()
                lista_de_cursos = ''
                for curso in cursos:
                        lista_de_cursos += curso.nombre + '\n'
                return lista_de_cursos
	

	def __unicode__(self):
		return self.correo_electronico


class Curso(models.Model):
	MODALIDAD = (
		('SE','Semanal'),
		('SA','Sabatino'),
	)
	nombre = models.CharField(max_length=64)
	descripcion = models.TextField()
	fechaInicio = models.DateField(auto_now=False)
	modalidad = models.CharField(max_length=2,choices=MODALIDAD)
	preRequisitos = models.TextField(null=True, blank=True)
	numeroHoras = models.SmallIntegerField()	
	costo_alumno_ipn = models.DecimalField(null=True, blank=True,max_digits=9, decimal_places=2)
	costo_empleado_ipn = models.DecimalField(null=True, blank=True,max_digits=9, decimal_places=2)
	costo_publico_general = models.DecimalField(null=True, blank=True,max_digits=9, decimal_places=2)
	temario = models.FileField(null=True, blank=True)
	alumnos_inscritos = models.ManyToManyField(Alumno, blank= True,null=True)
	def correo_alumnos_inscritos(self):
		alumnos =  self.alumnos_inscritos.all()
		correos = ''
		for alumno in alumnos:
			correos += alumno.correo_electronico + '\n'
		return correos

			
		

	def __unicode__(self):
		return self.nombre
#	def save(self, *args, **kwargs):
#		if not self.temario:
#			self.temario = None
#			self.descripcion = None
#			self.preRequisitos = None
#		super(Curso, self).save(*args, **kwargs)


