from django.contrib import admin
from .models import Order, OrderLineItem

# So within the admin.py of the checkout app, we need to add those models (models.py/checkout) we've just created. Otherwise, we would be unable to edit them through the admin panel. So we import Order and OrderLineItem.

# Register your models here.

# TabularInline subclass defines the template used to render the Order in the admin interface. StackedInline is another option

# 

class OrderLineAdminInline(admin.TabularInline):
  model = OrderLineItem

# create a class OrderAdmin, which inherits from the ModelAdmin of admin django
class OrderAdmin(admin.ModelAdmin):
  inlines = (OrderLineAdminInline, )

# we need to register both of these with the admin site so that we can edit them if necessary

admin.site.register(Order, OrderAdmin)

# Because we have created models, we have to do a makemigrations and then a migrate in the cmd terminal. And that will create the tables within our database.



