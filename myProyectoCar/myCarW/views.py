from django.shortcuts import render
from .models import SliderIndex

# debemos utilizar la tabla de Usuarios (User)
from django.contrib.auth.models import User
# importar las librerias de validacion (authenticated)
from django.contrib.auth import authenticate, logout, login as login_autent
# agregar un decorador  es para impedir el ingreso a una pagina del sitio
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    autos = SliderIndex.objects.all()
    return render(request,'web/index2.html',{'autos':autos})

def galeria(request):    
    return render(request,'web/galeria2.html')
    
@login_required(login_url='/login/')
def insumos(request):
    return render(request,'web/insumos.html')

def logout_vista(request):
    logout(request)
    autos = SliderIndex.objects.all()
    return render(request,'web/index2.html',{'autos':autos})

def login(request):
    if request.POST:
        usuario = request.POST.get("txtUser")
        password = request.POST.get("txtPass")
        us = authenticate(request, username=usuario,password=password)
        if us is not None and us.is_active:
            login_autent(request,us)
            autos = SliderIndex.objects.all()
            return render(request,'web/index2.html',{'user':us,'autos':autos})
        else:
            return render(request,'web/login.html',{'msg':'usuario / pass incorrecta'})        
    return render(request,'web/login.html')


def registro(request):
    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        usuario = request.POST.get("nomusuario")
        password = request.POST.get("contrasena")
        try:
            u = User.objects.get(username=usuario)
            return render(request,'web/registro2.html',{'msg':'existe usuario'})
        except:            
            u = User()
            u.username = usuario
            u.first_name = nombre
            u.last_name = apellido
            u.email = email
            u.set_password(password)
            u.save()

            us = authenticate(request, username=usuario,password=password)
            login_autent(request,us)
            autos = SliderIndex.objects.all()
            return render(request,'web/index2.html',{'user':us,'autos':autos})
    return render(request,'web/registro2.html')