from django.contrib import admin
from .models import Reviews


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "productname",
        "title",
        "reviews",
        "alias",
        "date",
    )
    
    ordering =('date',)


admin.site.register(Reviews,BlogAdmin)
