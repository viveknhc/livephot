# Import these methods
from urllib.request import urlopen
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import redirect, render
from .models import *

def index(request):
    print(request.POST)
    if request.method == 'POST':
        image = request.POST['imgurl']
        
    return render(request,"index.html")