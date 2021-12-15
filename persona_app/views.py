from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Persona
import requests
import json

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
    r = requests.get('https://randomuser.me/api?nat=fr')
    #jSon = json.dumps(r.text, indent=4)
    #f = open(jSon)
    #data = json.load(r.text) 
    jSon = r.json()['results']
    jSonData = jSon[0]
    newPersona = Persona()
    newPersona.first_name = jSonData['name']['first']
    newPersona.last_name = jSonData['name']['last']
    newPersona.address_street = jSonData['location']['street']['name']
    newPersona.address_number = jSonData['location']['street']['number']
    newPersona.city = jSonData['location']['city']
    newPersona.country = jSonData['location']['country']
    newPersona.postcode = jSonData['location']['postcode']
    newPersona.email = jSonData['email']
    newPersona.username = jSonData['login']['username']
    newPersona.password = jSonData['login']['password']
    newPersona.age = jSonData['dob']['age']
    newPersona.picture = jSonData['picture']['medium']
    newPersona.save()
    print(jSonData['location']['street']['name'])
    
    return redirect('details_persona',newPersona.id)