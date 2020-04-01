from django.shortcuts import render, redirect, reverse

# Create your views here.
# So this first view renders everything within the cart, all of the contents.So this is relatively straightforward, return render(request, "cart.html").And notice we don't have to pass in a dictionary of cart_contents because that context is available everywhere.

def view_cart(request):
  """A view that renders the cart contents page"""
  return render(request, 'cart.html')

# This takes an integer, and this gets an integer from the the form that we created in the last unit.So that will allow us to increase and decrease the number of items we want.And when we click on the Add to Cart button, the integer that is in that form will go to the cart.

def add_to_cart(request, id):
  """Add to quantity of the specified product to the cart. This takes an integer, and this gets an integer from the the form that we created in the last unit.And when we click on the Add to Cart button, the integer that is in that form will go to the cart."""
  quantity=int(request.POST.get('quantity'))
  # Now the cart here, you can see request.session, so it's not going to a database.It's going to get the cart from the session, and either gets a cart if one already exists or an empty dictionary if one does not yet exist.
  
  cart = request.session.get('cart', {})
  if id in cart:
    cart[id] = int(cart[id] + quantity)
  else:
    cart[id] = cart.get(id, quantity)

  request.session['cart'] = cart
  return redirect(reverse('index'))

def adjust_cart(request, id):
  """Adjust the quantity of the specified product to the specified amount"""
  quantity = int(request.POST.get('quantity'))
  cart = request.session.get('cart', {})

  # And of course, we can only adjust if a quantity is greater than 0.If there's nothing in the cart, you cannot adjust it.
  if quantity > 0:
    cart[id] = quantity
  else:
    cart.pop(id)
  
  request.session['cart'] = cart
  return redirect(reverse('view_cart'))





