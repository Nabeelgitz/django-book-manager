from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import BookDetail
from django.utils import timezone

# Create your views here.
# website/views.py


def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        author = request.POST.get("author")
        category = request.POST.get("category")
        date = request.POST.get("date")   # from input type="date"
        
        # Save to database
        BookDetail.objects.create(
            name=name,
            author=author,
            category=category,
            date=date
        )
        return redirect("home")  # after save, redirect to home page (or book list)
    
    return render(request, "library/add.html")

def remove(request, book_id=None):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        try:
            book = BookDetail.objects.get(pk=book_id)
            book.delete()
            return redirect("home")  # redirect to homepage after delete
        except BookDetail.DoesNotExist:
            return render(request, "library/remove.html", {
                "error": f"Book with ID {book_id} does not exist."
            })

    books = BookDetail.objects.all()
    return render(request, "library/remove.html", {"books": books})


def about(request):
    print("About page accessed")
    return render(request, "library/about.html")


def show(request):
    books = BookDetail.objects.all().order_by('-date')  # Latest first
    return render(request, "library/show.html", {"books": books})