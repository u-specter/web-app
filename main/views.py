from django.shortcuts import render

def index(request):
    data = {
        'title': 'Main page!',
        'values': ['asd', 'nur', 'mohi'],
        'obj': {
            'car': 'BMW',
            'age': 22,
            'hobby': 'Music'
        }
    }
    return render(request, 'main/index.html', data) 

def about(request):
    return render(request, 'main/about.html') 

