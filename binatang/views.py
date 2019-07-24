from django.shortcuts import render
from .models import NamaHewan as NamaHewanModel
from .forms import inputHewan

# Create your views here.
def NamaHewan(request):
    hewans = NamaHewanModel.objects.all()
    return render(request, 'daftar_binatang.html', {'hewan': hewans})

def listHewan2(request):
    list_hewan= Hewan.objects.all()
    return render(request, 'binatang.html',{'list_hewan':list_hewan})

def listHewan3(request):
    if request.method == 'POST':
        form = inputbinatang(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
    else:
        form = inputbinatang()
    return render(request, 'input_binatang.html',{'form':form})

