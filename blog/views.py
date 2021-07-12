from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reviews

from .forms import ReviewForm, CommentReviewForm

# Create your views here.

def blog(request):
    """ A view to return the blog_page"""

    reviews = Reviews.objects.all()
    
    context = {
        'reviews': reviews,
        }

    return render(request, 'blog/blog.html', context)

@login_required
def add_review(request):
    ''' 
    add a product to the store
    '''
    if not request.user:
        messages.error(request, f'Sorry only users can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, "New product successfully added!")
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed adding new review. Make sure form is valid!')
    else:
        form = ReviewForm()
    
    form = ReviewForm()
    template = "blog/addreview.html"

    context = {
        'form': form,
    }

    return render(request, template, context)



@login_required
def edit_review(request, review_id):
    ''' edit product in the store'''
    if not request.user.is_superuser:
        messages.error(request, f'Sorry only store owner can do that!')
        return redirect(reverse('home'))
        
    reviews = get_object_or_404(Reviews, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=reviews)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated review!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, f'Failed updating review!. Make sure form is valid!')
    else:
        form = ReviewForm(instance=reviews)
        messages.info(request, f'You are now editing {reviews.productname}')

    template = "blog/edit_review.html"
    context = {
        'reviews': reviews,
        'form': form,
    }

    return render(request, template, context)