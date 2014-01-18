from django.shortcuts import render
from models import Carrera, Alumno


# Create your views here.

def home(request):
	carrera = Carrera.objects.all()
	alumnos = Alumno.objects.all()
	return render(request,"index.html",locals())



def carrera(request):
	return render(request, "index.html", locals())