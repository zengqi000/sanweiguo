from django.shortcuts import render

# Create your views here.

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'login.html', context)

