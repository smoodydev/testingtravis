# Unlike the products app, where we created a model which then puts products into our database, in this case, the cart items will not go into the database.
# They will just be stored in the session when the user is logged in.
# So a user can add products to their cart, but when they log out, that cart will be lost.


from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
  """
  Ensures that the cart contents are available when rendering a page
  """
  """
  So we have a cart that requests the session.
  So it requests the existing cart if there is one, or a blank dictionary if there's not.
  """

  cart = request.session.get('cart', {})
# we then initialise cart_items
  cart_items = []
  total = 0
  product_count = 0
  # for loop takes 2 items: id and a quantity from the cart_items
  for id, quantity in cart.items():
    # we now get out products from our product model. And we use the primary key as our ID, as every product within our database will have a primary key, which is a unique ID.
    product = get_object_or_404(Product, pk=id)
    total += quantity * product.price
    product_count += quantity
    cart_items.append({'id': id, 'quantity': quantity, 'product': product})

  # we now return a dictionary, key value pairs

  return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }








