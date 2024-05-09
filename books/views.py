# Django imports
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from books.forms import BookForm, BookModelForm
from categories.models import Category


# python imports

 




# imports from your created files
from books.models import Book
# Create your views here.
# funntions views
def hello(request): 
    print(request)
    return HttpResponse("hi iam here")


def welcome(request):
    name="Haidy"
    return HttpResponse(f"<h1 style='color:red'>Welcome {name}</h1>")



books=[
{"id":1 , 'name':"Diamond Dust","price":100,"nums":450,"auther":"Ahmed Mourad","image":"image4.jpg"},
{"id":2 , 'name':"Rape but under one roof","price":120,"nums":500,"auther":"Doaa Abd Elrahman","image":"noval.png"},
{"id":3 , 'name':"Me, night and thoughts","price":100,"nums":350,"auther":"Ahmed Ashraf","image":"image3.jpg"},
{"id":4 , 'name':"Broken diamond","price":90,"nums":500,"auther":"Lyla Adel","image":"image6.jpg"},
]

 
def landing(request):
    return HttpResponse(books)

def book_details(request, id):
    filtered_books = filter(lambda book: book['id'] == id, books)
    all_books = list(filtered_books)
    if all_books:
        book = all_books[0]
        content = f"Id: {book['id']}, Name: {book['name']}, Price: {book['price']}, Image: {book['image']}"
        return HttpResponse(content)
    return HttpResponse("No product found")


def books_home(request):
# return with template home.html
 # render http response
 return render(request,"bookstore/home.html",
               context={"name":"haidy","books":books},
               status=200) 

def book_profile(request,id):
    filtered_books = filter(lambda book: book['id'] == id, books)
    filtered_books=list(filtered_books)
    if filtered_books:
       book= filtered_books[0]
       return render(request, "bookstore/details.html",
                     context={"book":book
                              })
    
def book_contact_us(request):
    return render(request, 'bookstore/contact_us.html')

def book_about_us(request):
    return render(request, 'bookstore/about_us.html')


    return HttpResponse("Book is not found")

def books_index(request):
    books = Book.objects.all()
    return render(request,"bookstore/crud/index.html",
            context={"books": books})


def book_show(request,id):
    # book=Book.objects.get(id=id)
    book = get_object_or_404(Book, pk=id)
    return render(request,"bookstore/crud/show.html",
                  context={"book": book})

def book_delete(request,id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    # return HttpResponse("Book deleted")
    return redirect(reverse("books_index"))


def book_create(request):
    print(request)
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        # Handling POST request
        print(request.POST)
        book= Book(name=request.POST["name"], price=request.POST["price"],
                nums=request.POST["nums"], author=request.POST["author"], 
                  code=request.POST["code"], image=image)
        book.save()
        return redirect(book.show_url)
        # return HttpResponse("Post request received") 
    
    # Handling GET request
    return render(request, 'bookstore/crud/create.html')





def book_update(request, id):
    # Retrieve the book object if it exists
    book = get_object_or_404(Book, pk=id)

    if request.method == "POST":
        # Extract data from the form
        name = request.POST.get("name")
        price = request.POST.get("price")
        nums = request.POST.get("nums")
        author = request.POST.get("author")
        code = request.POST.get("code")
        image = request.FILES.get("image")

        # Update the book object with new values
        book.name = name
        book.price = price
        book.nums = nums
        book.author = author
        book.code = code
        if image:
            book.image = image

        # Save the updated book object
        book.save()

        # Redirect to the book details page
        return redirect(book.show_url)

    # If it's a GET request, render the form with the existing book details
    return render(request, 'bookstore/crud/update.html', {'book': book})



def book_create_forms(request):
    form = BookForm()
    category = get_object_or_404(Category,pk=5)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            nums = form.cleaned_data['nums']
            author = form.cleaned_data['author']
            image = form.cleaned_data['image']
            code = form.cleaned_data['code']

            book = Book.objects.create(name=name, price=price, nums=nums, author=author, image=image, code=code, category=category)
            # book = form.save()
            return redirect(book.show_url)
    # else:
    #     form = BookForm()
    return render(request, 'bookstore/forms/create.html', context={'form': form})




def create_book_model_form(request):
    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect(book.show_url)
    else:
        form = BookModelForm()
    return render(request, 'bookstore/forms/createmodelform.html', {'form': form})



def edit_book(request, id):
    book= Book.get_books_by_id(id)
    form = BookModelForm(instance=book)

    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect(book.show_url)
    else:
        form = BookModelForm()
    return render(request, 'bookstore/forms/edit.html', {'form': form, 'book': book})

