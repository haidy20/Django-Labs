from django.shortcuts import render, redirect, reverse ,get_object_or_404
from django.http import HttpResponse
from categories.forms import CategoryModelForm
from categories.models import Category

# Create your views here.

def landing(request):
    return HttpResponse("<h1> Welcome to categories app </h1>")



def home(request):
    return render (request,"categories/home.html")


def create_category(request):
    form = CategoryModelForm()
    if request.method =="POST":
        form = CategoryModelForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            print("New category created:", category)  # Add this line for debugging

            url = reverse("categories.index")
            return redirect(url)

    return render(request,'categories/create.html',
                  context={'form': form})


def categories_index(request):
    categories = Category.get_all_categories()
    return render(request,'categories/index.html',
                  context={'categories':categories})


def category_show(request,id):
    category = get_object_or_404(Category, pk=id)
    return render(request,'categories/show.html',
                  context={'category':category})

# def show_category_details(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     return render(request, 'categories/category_details.html', {'category': category})
