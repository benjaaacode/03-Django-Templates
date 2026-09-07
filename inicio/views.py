from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio/inicio.html')

def App1v1(request):
    return render(request, 'inicio/App1v1.html')

def App1v2(request):
    return render(request, 'inicio/App1v2.html')