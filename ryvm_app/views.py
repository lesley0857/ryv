from django.shortcuts import render
from .models import *

# Create your views here.
def home_view(request):
    clergy_pic = picture_clergy.objects.all()
    context = {'clergy_pic':clergy_pic}
    return render(request,"home.html",context)
