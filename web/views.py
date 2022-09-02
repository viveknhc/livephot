# Import these methods
from urllib.request import urlopen
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import redirect, render
from .models import *
import base64

def index(request):
    print(request.POST)
    if request.method == 'POST':
        image = request.FILES['imgurl']
        base64_message = image.decode('ascii')
        Image.create(image=base64_message)  
    return render(request,"index.html")