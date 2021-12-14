from django.shortcuts import render

from django.http import HttpResponse
from .models import Persona

# Create your views here.
def persona_list(request):
    personas = Persona.objects.all().order_by('-id')
    context = {'personas':personas}
    return render(request,'persona_app/persona_list.html',context)
def persona_details(request,id):
    persona = Persona.objects.get(id=id)
    context = {'personas':persona}
    return render(request,'persona_app/persona_details.html',context)
def persona_generate(request):
    return HttpResponse("Persona_generate")