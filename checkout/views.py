from django.shortcuts import render, get_object_or_404, reverse, redirect

# We also are going to import auth.decorators login_required because you want your customer to be logged in when they actually purchase something.When they actually go to the checkout and say I want to pay, they should be logged in.
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import settings
from products.models import Product
from stripe

# Create your views here.

# the view will require the api keys

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
  if request.method=='POST':
    order_form = OrderForm(request.POST)
    payment_form = MakePaymentForm(request.POST)

    if order_form.is_valid() and payment_form.is_valid():
      order = order_form.save(commit=False)
      order.date = timezone.now()
      order.save()
      # u neeed to get the info on what is being purchased. we will get that from variable cart
      cart = request.session.get('cart' {})
      # initialise a total of zero
      total = 0
      # then do a for loop
      for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        order_line_item = OrderLineItem(
          order = order,
          product = product,
          quantity = quantity
        )
        order_line_item.save()

      # now we know what they want to buy we now introduce a try except. try except will create a customer charge

      try:
        customer = stripe.Charge.create(
          amount = int(total * 100),
          currency = 'EUR',
          description = request.user.email,
          # we also need a stripe id from that form
          card = payment_form.cleaned_data['stripe_id'],
        )
        # if card declined:

      except stripe.error.CardError:
        messages.error(request, 'Your card was declined')

      if customer.paid:
        messages.error(request, 'You have successfully paid')
        request.session['cart'] = {}
        return redirect(reverse('products'))
      else:
        messages.error(request, 'Unable to take payment')
    else:
      print(payment_form.errors)
      messages.error(request, 'We were unable to take a payment with that card')
  else:
    payment_form = MakePaymentForm()
    order_form = OrderForm()

  return render(request, 'checkout.html', {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})





