from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Companyinfo

from .forms import CompanyinfoForm


# Create your views here.

def Companyinfopage(request):
    """ A view to return the blog_page"""

    companyinfo = Companyinfo.objects.all()
    
    context = {
        'companyinfo': companyinfo,
        }

    return render(request, context, 'companyinfo/companyinfo.html')
