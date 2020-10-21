from django.shortcuts import render
from .models import SliderIndex,Insumos

# debemos utilizar la tabla de Usuarios (User)
from django.contrib.auth.models import User
# importar las librerias de validacion (authenticated)
from django.contrib.auth import authenticate, logout, login as login_autent
# agregar un decorador  es para impedir el ingreso a una pagina del sitio
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    autos = SliderIndex.objects.all()
    return render(request,'web/index2.html',{'autos':autos})

def galeria(request):    
    return render(request,'web/galeria2.html')

@login_required(login_url='/login/')
@permission_required('myCarW.change_insumos',login_url='/login/')
@permission_required('myCarW.view_insumos',login_url='/login/')
def modificar_insumos(request):
    if request.POST:
        nombre = request.POST.get("nombreinsumo")
        precio = request.POST.get("precio")
        desc = request.POST.get("descripcion")
        stock = request.POST.get("stock")
        try:
            insumo = Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = desc
            insumo.stock = stock
            insumo.save()
            msg ='Actualizo'
        except:
            msg='No Modifico Reg.'
    insumos = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'insumos':insumos,'msg':msg})



@login_required(login_url='/login/')
@permission_required('myCarW.view_insumos',login_url='/login/')
def modificar_vista(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'web/insumos_mod.html',{'insumo':insumo})
    except:
        msg ="No Existe Insumo"
    insumos = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'insumos':insumos,'msg':msg})  
    

@login_required(login_url='/login/')
@permission_required('myCarW.delete_insumos',login_url='/login/')
def eliminar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg ="Insumo Eliminado"
    except:
        msg="No Elimino Insumo"
    insumos = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'insumos':insumos,'msg':msg})  
    

@permission_required('myCarW.view_insumos',login_url='/login/')
def admin_insumos(request):
    insumos = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'insumos':insumos})

@login_required(login_url='/login/')
@permission_required('myCarW.add_insumos',login_url='/login/')
@permission_required('myCarW.change_insumos',login_url='/login/')
def insumos(request):
    if request.POST:
        nombre = request.POST.get("nombreinsumo")
        precio = request.POST.get("precio")
        desc = request.POST.get("descripcion")
        stock = request.POST.get("stock")

        insumo = Insumos(
            nombre=nombre,
            precio=precio,
            descripcion=desc,
            stock=stock
        )
        insumo.save()
        return render(request,'web/insumos.html',{'msg':'insumo grabado'})
        
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