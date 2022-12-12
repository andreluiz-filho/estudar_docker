import os
from django.http import HttpResponse

def hello_world(request):
      return HttpResponse("<h1>Ola man !!!  aaa</h1>")
