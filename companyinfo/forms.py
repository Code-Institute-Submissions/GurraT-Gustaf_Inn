from django import forms
from .models import Companyinfo


class CompanyinfoForm(forms.ModelForm):

    class Meta:
        model = Companyinfo
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        companyinfo = Companyinfo.objects.all()