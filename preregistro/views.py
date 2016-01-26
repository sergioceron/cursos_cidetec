from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

from datetime import date
from preregistro.models import Curso
from preregistro.models import Alumno
from preregistro.forms import AlumnoFormulario


def index(request):
	ultimos_cursos_lista = Curso.objects.filter(fechaInicio__gte = date.today()).order_by('fechaInicio')
	context = {'ultimos_cursos_lista': ultimos_cursos_lista}
	return render(request,'preregistro/index.html',context)


def registro(request,curso_id):
	curso = get_object_or_404(Curso,pk=curso_id)
	
	if request.method == 'POST':
		formularioAlumno = AlumnoFormulario(request.POST)
		
		if formularioAlumno.is_valid():
			nombre = formularioAlumno.cleaned_data['nombre']
			apellido_paterno = formularioAlumno.cleaned_data['apellido_paterno']
			apellido_materno = formularioAlumno.cleaned_data['apellido_materno']
			correoElectronico = formularioAlumno.cleaned_data['correo_electronico']
			tipo = formularioAlumno.cleaned_data['tipo']

			try: 
				alumno = Alumno.objects.get(correo_electronico = correoElectronico)
			except:
				alumno = formularioAlumno.save()

			try:
				alumnoIncrito = Curso.objects.get(nombre = curso.nombre, alumnos_inscritos=alumno)
				
				return render(request,'preregistro/registroPrevio.html',{'curso':curso,'correo_electronico':correoElectronico})
				return HttpResponse("Alumno " + alumno.correo_electronico + " ya incrito a estecurso")
			except:
				curso.alumnos_inscritos.add(alumno)
				alumno.cursos_inscritos.add(curso)
			
			
				return render(request,'preregistro/registroExitoso.html',{'curso':curso,'correo_electronico':correoElectronico})
	else:
		formularioAlumno = AlumnoFormulario()


	return render(request,'preregistro/registro.html',{'curso':curso,'formularioAlumno':formularioAlumno})

	
