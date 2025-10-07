from django.shortcuts import render
from django.http import HttpResponse
from library.models import BookDetail

# Create your views 


def home(request):
    print("Home page accessed")
    books = BookDetail.objects.all().order_by('-date')  # latest first
    return render(request, 'website/home.html', {'books': books})
