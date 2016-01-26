from django.db import models
from django.forms import ModelForm
from preregistro.models import Alumno


class AlumnoFormulario(ModelForm):
	class Meta:
		model = Alumno
		fields = ['nombre','apellido_paterno','apellido_materno','tipo','correo_electronico']
	
