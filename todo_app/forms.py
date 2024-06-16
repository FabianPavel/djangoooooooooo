from django import forms
from .models import Klient, Pokoj, Rezervace

class KlientForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = ['jmeno', 'prijmeni', 'email', 'telefonni_cislo', 'adresa']

class PokojForm(forms.ModelForm):
    class Meta:
        model = Pokoj
        fields = ['cislo_pokoje', 'typ_pokoje', 'popis', 'cena_za_noc', 'obrazek']

class RezervaceForm(forms.ModelForm):
    class Meta:
        model = Rezervace
        fields = ['klient', 'pokoj', 'datum_prijezdu', 'datum_odjezdu']
