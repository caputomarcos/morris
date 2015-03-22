from django.shortcuts import render
from django.views.generic import ListView
from .models import Person


def index(request):
    return render(request, "index.html")


def download(request):
    return render(request, "download.html")


def about(request):
    return render(request, "about.html")


def morris(request):
    return render(request, "core/morris.html")


class MorrisDataView(ListView):
    template_name = 'core/morris_data.html'
    model = Person

# pessoas por uf
# porcentagem de gender
# porcentagem de active
# por faixa etária 10 em 10
