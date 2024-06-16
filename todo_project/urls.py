from django.contrib import admin
from django.urls import path
from todo_app.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add_klient/', add_klient, name='add_klient'),
    path('add_pokoj/', add_pokoj, name='add_pokoj'),
    path('add_rezervace/', add_rezervace, name='add_rezervace'),

    path('pokoje/', get_pokoje, name='get_pokoje'),
    path('klienti/', get_klienti, name='get_klienti'),
    path('rezervace/', get_rezervace, name='get_rezervace'),

    path('api/pokoj/<int:pokoj_id>/cena/', get_pokoj_cena, name='pokoj-cena'),

    path('rezervace/odstranit/<int:pk>/', odstranit_rezervaci, name='odstranit_rezervaci'),
    path('pokoj/odstranit/<int:pk>/', odstranit_pokoj, name='odstranit_pokoj'),
    path('klient/odstranit/<int:pk>/', odstranit_klienta, name='odstranit_klienta'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


