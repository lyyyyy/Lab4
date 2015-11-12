
# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from lib_manage.models import Book,Author
from django.template import Context
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(now)
    
def current_datetime2(request):
    now = datetime.datetime.now()
    c = Context({'time':now})
    return render_to_response("time.html", c)
    
def main(request):
    return render_to_response("welcome.html")
    
def addBook(request):
    if request.POST:
        post = request.POST
        try:
            authorid = Author.objects.get(Name = post["Authorname"])
            new_Book = Book(
                Title = post["Title"],
                AuthorID = authorid,
                Publisher = post["Publisher"],
                PublishDate = post["PublishDate"], 
                Price = post["Price"]
                )
            new_Book.save()
            #q = Author.AuthorID()
            
            return HttpResponseRedirect("/addBook/") 
        except ObjectDoesNotExist:
             return HttpResponseRedirect("/addAuthor/") 
        

    return render_to_response("addbook.html")
    
def addAuthor(request):
    if request.POST:
        post = request.POST
        new_Author = Author(  
            Name = post["Name"],
            Age = post["Age"],
            Country = post["Country"]    
        )
        new_Author.save()  
        return HttpResponseRedirect("/addBook/") 
    return render_to_response("addAuthor.html")


def Search(request):
    if 'query' in request.GET and request.GET['query']:
        tmp = request.GET['query']
        try:
            person = Author.objects.get(Name = tmp)#模糊查找
            book_list = person.book_set.all()
            c = Context({"book_list":book_list,"query":person.Name,})
        except ObjectDoesNotExist:
            book_list = None
            person = None
            c = Context({"book_list":book_list,"query":person,})
        return render_to_response('AllBooks.html', c)
        #showBooks(tmp)
    return render_to_response('Search.html')

#def showBooks(request):
    #global tmp

    
def details(request):
    ID = request.GET["id"]
    book = Book.objects.get(ISBN = ID)
    #author = Author.objects.filter(AuthorID = book.AuthorID.AuthorID)
    author = book.AuthorID
    c = Context({"book":book,"author":author,})
    return render_to_response('details.html',c)
            
def delete(request):
    ID = request.GET["id"]
    book = Book.objects.get(ISBN = ID)
    #author = Author.objects.filter(AuthorID = book.AuthorID.AuthorID)
    author = book.AuthorID
    book.delete()
    try:
        Book.objects.filter(AuthorID = author.AuthorID)
    except ObjectDoesNotExist:
        author.delete()
    return HttpResponseRedirect("/search/")
        
def update(request):
    ID  = request.GET["id"]
    book = Book.objects.get(ISBN = ID)
    author = book.AuthorID
    if request.POST:
        post = request.POST
        #book.AuthorID = author
        book.Publisher = post["Publisher"]
        book.PublishDate = post["PublishDate"]
        book.Price = post["Price"]
        #author.AuthorID = post["AuthorID"]
        author.Name = post["Name"]
        author.Age = post["Age"]
        author.Country = post["Country"] 
    book.save()
    author.save()
    return render_to_response('update.html')
    
    
    
    
