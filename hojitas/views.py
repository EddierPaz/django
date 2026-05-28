from django.shortcuts import render, redirect, get_object_or_404
from .models import Hojas

def home(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def crear_hojita(request):
    if request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        imagen = request.FILES["imagen"]
        description = request.POST["description"]

        hojita = Hojas(name=name, price=price, imagen=imagen, description=description)
        hojita.save()

        # Ojo: revisa si tu ruta principal se llama 'index' o 'inicio' en tus urls.py
        return redirect("lista_hojitas") 

    # Solución: Quitamos el {"hojita": None} para evitar el conflicto de Python
    return render(request, "hojitas/CRUD/crear.html")


def editar_hojita(request, id):
    hojita = get_object_or_404(Hojas, id=id)

    if request.method == "POST":
        hojita.name = request.POST["name"]
        hojita.price = request.POST["price"]
        hojita.description = request.POST["description"]

        if "imagen" in request.FILES:
            hojita.imagen = request.FILES["imagen"]

        hojita.save()

        return redirect("lista_hojitas")

    return render(request, "hojitas/CRUD/editar.html", {"hojita": hojita})

def lista_hojitas(request):
    hojitas = Hojas.objects.all()
    return render(request, "index.html", {"hojas": hojitas})

def eliminar_hojitas(request, id):
    hojita = get_object_or_404(Hojas, id=id)
    hojita.delete()
    return redirect('lista_hojitas')