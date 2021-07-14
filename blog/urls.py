from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add/', views.add_review, name='add_review'),
<<<<<<< HEAD
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
=======
    #path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
>>>>>>> 02c3a0e493943218c9b52183ff524a90dd889041
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),

]
