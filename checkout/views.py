from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    # check there is content in the bag
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PAtzyCJWWbRusAzYidbEzFENaHei3EYMCDdO1NhDMLZ180875HVDw4cxcAaiuw1McFGGFG8xAz9sDJC6iYh0rXR00bx71eON4',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
