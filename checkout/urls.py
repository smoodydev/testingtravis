from django.conf.urls import url
from .views import checkout

# Its a very simple URL that just goes to the checkout view
# after u type urlpatterns here u go to import it into our main URLs whhich in this project is in the eccommerce urls.py file 
urlpatterns = [
  url(r'^$', checkout, name='checkout'),
]