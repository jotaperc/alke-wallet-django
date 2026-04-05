from django.shortcuts import render, redirect
from .models import Usuario

def lista_usuarios(request):
    # LEER (Read): Obtenemos todos los registros de la base de datos
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    # CREAR (Create): Si el usuario envía el formulario
    if request.method == 'POST':
        nombre_web = request.POST.get('nombre')
        correo_web = request.POST.get('correo')
        # Guardamos en la BD usando el ORM
        Usuario.objects.create(nombre=nombre_web, correo=correo_web)
        return redirect('lista_usuarios')
    return render(request, 'crear_usuario.html')