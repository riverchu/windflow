from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show(request):
    content = {}
    content['user'] = 'Tom'
    return render(request, 'info/index.html', content)

