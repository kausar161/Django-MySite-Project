from django.shortcuts import render

from django.http import HttpResponse
 

#from .models import Book

# Create your views here.

def index(request):
    return HttpResponse("HELLO NOYON WELCOME TO THE DJANGO WORLD")

    #def book_by_id(request,book_id):
       # book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book})
       # return HttpResponse(f"Book: {book.title},published on {book.pub_date}")

   # def index(request):
       # return HttpResponse( "Home.html")



