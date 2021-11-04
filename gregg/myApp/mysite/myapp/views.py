from django.shortcuts import render

def hello(request, name='world'):
    if request.method == 'GET':
        return render(request, 'hello.html', { 'name': name })

def goodbye(request):
    if request.method == 'GET':
        return render(request, 'goodbye.html')