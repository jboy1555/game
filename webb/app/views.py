from django.shortcuts import render
from django.http import HttpResponse
from . import views

def newindex(request):
    return render(request, 'app/newindex.html')
def main(request):
    return render(request, 'app/main.html')
