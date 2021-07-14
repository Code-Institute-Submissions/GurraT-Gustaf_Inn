from django.contrib import admin
from .models import Companyinfo


class CompanyinfoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "news",
        "date",
    )

    ordering =('date',)

admin.site.register(Companyinfo,CompanyinfoAdmin)