from django.shortcuts import render

def index(request):
    return render(request, 'spa_app/main.html')

def about(request):
    return render(request, 'spa_app/about.html')

def services(request):
    return render(request, 'spa_app/services.html')

def contact(request):
    return render(request, 'spa_app/contact.html')
