from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .models import Order, OrderLineItem
from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.warning(request, 'Your bag is empty at the moment')
        return redirect(reverse('products'))
    
    current_bag =bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order = Order.objects.all()
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'order': order,
        'stripe_public_key' : 'pk_test_51IqicmJkdyXzLxmX6JMO0yvSUBSoBQQH55IEhBkFS2t29G8H8DyLvQqVsT4ExZ8BuQiVvJd78EBZ46RSrZjFhOXI005WNVmLp2',
        'client_secret' : 'test client secret',
    }
    
    return render(request, template, context)


