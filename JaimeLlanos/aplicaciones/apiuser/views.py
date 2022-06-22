from django.shortcuts import redirect, render
from .models import Jaime
from .forms import PersonaForm

def inicio(request):
    users = Jaime.objects.all()
    contexto = {
        'users':users
    }
    return render(request,'index.html',contexto)

def createUser(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crearpersona.html',contexto)

def editarUser(request,id):
    users = Jaime.objects.get(id_user = id)
    if request.method == 'GET':
        form = PersonaForm(instance=users)
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST, instance=users)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crearpersona.html',contexto)

def eliminarUser(request,id):
    users= Jaime.objects.get(id_user = id)
    users.delete()
    return redirect('index')