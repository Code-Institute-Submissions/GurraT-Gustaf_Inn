from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import Order, OrderLineItem
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.warning(request, 'Your bag is empty at the moment')
        return redirect(reverse('products'))
    
    order = Order.objects.all()
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'order': order
    }
    
    return render(request, template, context)


