
from django.shortcuts import render
#from .models import *
from .models import *
# Create your views here.
def home_view(request):
    state = States.objects.get(state_id=25)
    lga = Lga.objects.all()
    context = {'lga':lga}
    return render(request,"index.html",context)

def ward_view(request,id):
    ward = Ward.objects.filter(lga_id=id)
    context = {'ward':ward}
    return render(request,"index.html",context)

def pu_view(request,id):
    wardd = Ward.objects.get(uniqueid=id)
    pu = PollingUnit.objects.filter(ward_id=id)
    context = {'pu':pu,"wardd":wardd}
    return render(request,"index.html",context)

def pur_view(request,id):
    pur = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=id)
    context = {'pur':pur}
    return render(request,"index.html",context)

def tu_view(request,id):
    tu = PollingUnit.objects.filter(lga_id=id)
    context = {'tu':tu}
    return render(request,"index.html",context)