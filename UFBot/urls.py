"""UFBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.http import JsonResponse
from urllib.request import Request, urlopen
import requests

def get_uf(request):
    url = "https://www.uf-hoy.com/"
    site = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(site.text, features="html5lib")
    value = soup.find("input", {"id": "caja1"})
    uf = float(value["value"].replace(".","").replace(",", "."))
    return HttpResponse(f'UF,"{uf}"')

urlpatterns = [
    path('get_uf/', get_uf)
]
