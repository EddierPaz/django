from django.shortcuts import render, redirect, get_object_or_404
from .models import Hojas

# Vista para la página de inicio (Index)
def home(request):
    # Consultamos las hojas para que el inicio no aparezca vacío
    hojitas = Hojas.objects.all()
    return render(request, 'index.html', {"hojas": hojitas})

def nosotros(request):
    return render(request, "paginas/nosotros.html")

# Vista para Crear
def crear_hojita(request):
    if request.method == "POST":
        nombre = request.POST["name"]
        precio = request.POST["price"]
        imagen = request.FILES.get("imagen")
        descripcion = request.POST["description"]

        # Guardamos usando los nombres de tu modelo en español
        hojita = Hojas(nombre=nombre, precio=precio, imagen=imagen, descripcion=descripcion)
        hojita.save()
        return redirect("index")

    return render(request, "hojitas/CRUD/crear.html")

# Vista para Editar
def editar_hojita(request, id):
    hojita = get_object_or_404(Hojas, id=id)

    if request.method == "POST":
        hojita.nombre = request.POST["name"]
        hojita.precio = request.POST["price"]
        hojita.descripcion = request.POST["description"]

        if "imagen" in request.FILES:
            hojita.imagen = request.FILES["imagen"]

        hojita.save()
        return redirect("index")

    return render(request, "hojitas/CRUD/editar.html", {"hojita": hojita})

# Vista para Listar
def lista_hojitas(request):
    hojitas = Hojas.objects.all()
    return render(request, "hojitas/CRUD/listar.html", {"hojas": hojitas})

# Vista para Eliminar
def eliminar_hojitas(request, id):
    hojita = get_object_or_404(Hojas, id=id)
    hojita.delete()
    return redirect('lista_hojitas')