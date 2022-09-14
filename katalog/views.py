from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_CatalogItem = CatalogItem.objects.all()
    context = {
        'list_Catalog': data_CatalogItem,
        'name': 'Ariya',
        'studentid' : '2106751991'
    }
    return render(request, "katalog.html", context)