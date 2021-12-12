from django.shortcuts import render

# Create your views here.


def bienvenido(request):
    return render(request, "inicio/index.html", {})

def probando(request):
    return render(request, "inicio/bienvenido_prueba.html", {})

def contacto(request):
    contexto={"Nombre:" : "Axel",
                "lista_de_numeros": [1254, 5687, 87554, 150, 2500, 1900],
                "edad": 17, 
                }  
    return render(request, "inicio/contacto.html", contexto)
    

