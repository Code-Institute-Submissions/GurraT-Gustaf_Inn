from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} to quantity of {bag[item_id]} pcs')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)

    if 'quantity' in request.POST:
        quantity = int(request.POST.get('quantity'))
    request.session['bag'] = bag

    if quantity:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} to quantity of {bag[item_id]} pcs')
        else:
            del bag[item_id]['quantity']
            messages.success(request, f'Removed {product.name} from your bag')
            if not bag[item_id]['quantity']:
                bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} to quantity of {bag[item_id]} pcs')

        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')


    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    
    try:
        bag = request.session.get('bag', {})
        product = get_object_or_404(Product, pk=item_id)

        if 'item_id' in request.POST:
            item_id = request.POST['item_id']
       
        if 'item_id' in request.POST:
            del bag[item_id]
            if not bag[item_id]:
                bag.pop(item_id)
                messages.success(request, f'Removed {product.name} from your bag')

        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')


        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

