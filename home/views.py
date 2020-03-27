from django.shortcuts import render

# Create your views here.

# a view that will render a html page

def index(request):
  """A view that displays the index page"""
  return render(request, 'index.html')
