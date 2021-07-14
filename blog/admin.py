from django.contrib import admin
from .models import Reviews, CommentReviews


class CommentAdminInline(admin.TabularInline):
    model = CommentReviews
    readonly_fields = ('comments',)


class BlogAdmin(admin.ModelAdmin):
    
    inlines= (CommentAdminInline,)

    list_display = (
        "productname",
        "title",
        "reviews",
        "alias",
        "date",
    )
    
    ordering =('date',)



admin.site.register(Reviews,BlogAdmin)

