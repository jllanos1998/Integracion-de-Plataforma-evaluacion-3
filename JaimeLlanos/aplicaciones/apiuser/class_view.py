from msilib.schema import Class
from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .forms import PersonaForm
from .models import Jaime
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class ApiView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):

        if(id>0):
            obj = list(Jaime.objects.filter(id_user = id).values())
            if len(obj) > 0:
                user = obj[0]
                datos = {'message':"Succes",'user':user}
            else:
                datos = {'message':"user not found..."}
            return JsonResponse(datos)
        if(id == 0):
            users = list(Jaime.objects.values())
            if len(users) > 0:
                datos = {'message':"Succes",'user':users}
            else:
                datos = {'message':"user not found..."}
            return JsonResponse(datos)
    def post(self, request):
        data = json.loads(request.body)
        Jaime.objects.create(
            nombre=data['nombre'],
            apellido=data['apellido'],
            edad=data['edad'],
            sexo=data['sexo'],
            telefono=data['telefono'],
            direccion=data['direccion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        data = json.loads(request.body)
        objlist = list(Jaime.objects.filter(id_user=id).values())
        if len(objlist) > 0:
            obj = Jaime.objects.get(id_user=id)
            obj.nombre = data['nombre'] 
            obj.apellido = data['apellido']
            obj.edad = data['edad']
            obj.sexo = data['sexo']
            obj.telefono = data['telefono']
            obj.direccion = data['direccion']
            obj.save()
            datos = {'message': "Success"}
        else:   
            datos= {'message':"user not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        objs = list(Jaime.objects.filter(id_user=id).values())
        if len(objs) > 0:
            Jaime.objects.filter(id_user=id).delete()
            datos = {'message': "Deleted"}
        else:   
            datos= {'message':"user not found..."}
        return JsonResponse(datos)

class UserList(ListView):
    model = Jaime
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.all()
    
class UserCreate(CreateView):
    model = Jaime
    form_class = PersonaForm
    template_name = 'crearpersona.html'
    success_url = reverse_lazy('index')

class UserUpdate(UpdateView):
    model = Jaime
    form_class = PersonaForm
    template_name = 'crearpersona.html'
    success_url = reverse_lazy('index')

class UserDelete(DeleteView):
    model = Jaime
    template_name= 'verificacion.html'
    success_url = reverse_lazy('index')