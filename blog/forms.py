from django import forms
from .models import Reviews, CommentReviews


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        reviews = Reviews.objects.all()


class CommentReviewForm(forms.ModelForm):
    # not in use at the moment could be used for adding comments to reviews

    class Meta:
        model = CommentReviews
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        commentreviews = CommentReviews.objects.all()