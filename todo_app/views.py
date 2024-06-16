from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import *
from .models import *

def home(request):
    return render(request, 'home.html')

def add_klient(request):
    if request.method == 'POST':
        form = KlientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = KlientForm()
    return render(request, 'add/add_klient.html', {'form': form})

def add_pokoj(request, pk=None):
    if request.method == 'POST':
        form = PokojForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PokojForm()
    return render(request, 'add/add_pokoj.html', {'form': form})

def add_rezervace(request):
    if request.method == 'POST':
        form = RezervaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RezervaceForm()
    return render(request, 'add/add_rezervace.html', {'form': form})

def get_pokoje(request):
    pokoje = Pokoj.objects.all()
    return render(request, 'pokoje.html', {'pokoje': pokoje})

def get_klienti(request):
    klienti = Klient.objects.all()
    return render(request, 'klienti.html', {'klienti': klienti})

def get_rezervace(request):
    rezervace = Rezervace.objects.all()
    return render(request, 'rezervace.html', {'rezervace': rezervace})

def get_pokoj_cena(request, pokoj_id):
    pokoj = Pokoj.objects.get(id=pokoj_id)
    return JsonResponse({"cena_za_noc": pokoj.cena_za_noc})

@require_POST
def odstranit_rezervaci(request, pk):
    rezervace = get_object_or_404(Rezervace, pk=pk)
    rezervace.delete()
    return redirect('get_rezervace')

@require_POST
def odstranit_klienta(request, pk):
    klient = get_object_or_404(Klient, pk=pk)
    klient.delete()
    return redirect('get_klienti')

@require_POST
def odstranit_pokoj(request, pk):
    pokoj = get_object_or_404(Pokoj, pk=pk)
    pokoj.delete()
    return redirect('get_pokoje')
