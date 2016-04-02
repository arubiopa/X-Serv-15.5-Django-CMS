from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
# Create your views here.
def cms(request, recurso):
    try:
		contenido = Pages.objects.get(name=recurso)
		return HttpResponse(contenido.name+ ':' + contenido.page)
	except Pages.DoesNotExist:
		return HttpResponse("Recurso no encontrado: " + recurso)
