from django.contrib import admin
from .models import Reviews, CommentReviews


class CommentAdminInline(admin.TabularInline):
    # not in use at the moment could be used for adding comments to reviews
    model = CommentReviews
    readonly_fields = ('comments',)


class BlogAdmin(admin.ModelAdmin):
    # inlines not in use at the moment could be used for adding comments to reviews
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

