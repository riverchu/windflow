from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def manage(request):
    content = {}
    content['user'] = 'Tom'
    return render(request, 'armory/index.html', content)
