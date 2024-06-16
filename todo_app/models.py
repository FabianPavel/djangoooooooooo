from django.db import models
from django.conf import settings
import datetime

class Klient(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=100, verbose_name="Příjmení")
    email = models.EmailField(unique=True, verbose_name="Email")
    telefonni_cislo = models.CharField(max_length=15, verbose_name="Telefonní číslo")
    adresa = models.CharField(max_length=50, verbose_name="Adresa")

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienti"

class Pokoj(models.Model):
    JEDNOLUZKOVY = '1L'
    DVOLUZKOVY = '2L'
    APARTMA = 'AP'
    TYP_POKOJE_CHOICES = [
        (JEDNOLUZKOVY, 'Jednolůžkový'),
        (DVOLUZKOVY, 'Dvoulůžkový'),
        (APARTMA, 'Apartmá')
    ]
    cislo_pokoje = models.CharField(max_length=10, unique=True, verbose_name="Číslo pokoje")
    typ_pokoje = models.CharField(max_length=2, choices=TYP_POKOJE_CHOICES, default=JEDNOLUZKOVY, verbose_name="Typ pokoje")
    popis = models.TextField(verbose_name="Popis", blank=True, null=True)
    cena_za_noc = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Cena za noc")
    obrazek = models.ImageField(upload_to='../', blank=True, null=True, verbose_name="Obrázek")

    def __str__(self):
        return f"{self.cislo_pokoje} ({self.get_typ_pokoje_display()})"

    class Meta:
        verbose_name = "Pokoj"
        verbose_name_plural = "Pokoje"

class Rezervace(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE, verbose_name="Klient")
    pokoj = models.ForeignKey(Pokoj, on_delete=models.CASCADE, verbose_name="Pokoj")
    datum_prijezdu = models.DateField(verbose_name="Datum příjezdu")
    datum_odjezdu = models.DateField(verbose_name="Datum odjezdu")
    celkova_cena = models.DecimalField(max_digits=10, decimal_places=2, editable=False, verbose_name="Celková cena")

    def save(self, *args, **kwargs):
        self.celkova_cena = self.calculate_total_price()
        super().save(*args, **kwargs)

    def calculate_total_price(self):
        cena_za_noc = self.pokoj.cena_za_noc
        pocet_dni = (self.datum_odjezdu - self.datum_prijezdu).days
        return cena_za_noc * pocet_dni

    def __str__(self):
        return f"{self.klient} - {self.pokoj} od {self.datum_prijezdu} do {self.datum_odjezdu}"

    class Meta:
        verbose_name = "Rezervace"
        verbose_name_plural = "Rezervace"
