from django.contrib import admin
from models import Curso,Alumno

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion','fechaInicio','modalidad','numeroHoras','preRequisitos','costo_alumno_ipn','costo_empleado_ipn','costo_publico_general','temario','correo_alumnos_inscritos')
	search_fields = ['nombre']
	filter_horizontal = ('alumnos_inscritos',)

class AlumnoAdmin(admin.ModelAdmin):
	list_display = ('correo_electronico','nombre','apellido_paterno','apellido_materno','tipo','cursos_inscritos_anteriormente')
	filter_horizontal = ('cursos_inscritos',)
	search_fields = ['correo_electronico']

admin.site.register(Curso,CursoAdmin)
admin.site.register(Alumno,AlumnoAdmin)
