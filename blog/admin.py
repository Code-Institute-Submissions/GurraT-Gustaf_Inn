from django.contrib import admin
from .models import Reviews, CommentReviews


class CommentAdminInline(admin.TabularInline):
<<<<<<< HEAD
=======
    # not in use at the moment could be used for adding comments to reviews
>>>>>>> 02c3a0e493943218c9b52183ff524a90dd889041
    model = CommentReviews
    readonly_fields = ('comments',)


class BlogAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    
=======
    # inlines not in use at the moment could be used for adding comments to reviews
>>>>>>> 02c3a0e493943218c9b52183ff524a90dd889041
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

