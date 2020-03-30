from django.conf.urls import url, include
from .views import all_products

"""
  So we have a straightforward URL here, which will just show the all_products view.
  And we've given it name='products'.
  """
urlpatterns = [
  url(r'^$', all_products, name='products'),
  
]