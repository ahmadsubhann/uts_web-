# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def members(request):
  template = loader.get_template('menu.html')
  return HttpResponse(template.render())
def kategori(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())