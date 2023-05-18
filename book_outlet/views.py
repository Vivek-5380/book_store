from django.shortcuts import render , get_object_or_404
from .models import book
from django.db.models import Avg

# Create your views here.

def index(request):
    books = book.objects.all().order_by("-title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request , "book_outlet/index.html", {
        "books" : books,
        "tbn" : num_books,
        "average_rating" : avg_rating,
    })
    
def book_details(request , slug):
    book_fetch = get_object_or_404(book,slug=slug)
    return render(request, "book_outlet/book_detail.html" , {
        "title" : book_fetch.title,
        "rating" : book_fetch.rating,
        "is_bestseller" : book_fetch.is_bestselling,
    })