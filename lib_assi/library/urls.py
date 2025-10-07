from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path("remove/", views.remove, name="remove"),
    path('about/', views.about, name='about'),   # fixed
    path('show/', views.show, name='show'),  # Home page to show all books
]
