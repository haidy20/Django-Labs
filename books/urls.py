from django.urls import path
from books.views import hello,welcome,landing,book_details,books_home,book_profile,book_contact_us,book_about_us,books_index,book_show,book_delete,book_create,book_update,book_create_forms,create_book_model_form,edit_book



urlpatterns = [
    path('hello', hello, name='hellopage'),
    path('wlcm',welcome,name='welcomepage'),
    path('land',landing,name='books'),
    # specify part of the URL --> variable and must be int
    # path('book/<int:id>',book_details,name='bok.datails'),
    path('books/<int:id>/', book_details, name='book_details'),
    path('home',books_home,name='books.home'),
    path('old/<int:id>', book_profile,name='book_profile'),

    path('contact/', book_contact_us, name='contact_us'),
    path('about/', book_about_us, name='about_us'),
    path('',books_index,name='books_index'),
    path('<int:id>',book_show,name='books.show'),
    path('<int:id>/delete',book_delete,name='books.delete'),
    path('create',book_create,name='books.create'),
    path('<int:id>/update/', book_update, name='books.update'),
    path('form/create',book_create_forms, name='books.create.forms'),
    path('forms/createmodelform', create_book_model_form, name='books.createmodel'),
    path('forms/<int:id>/edit',edit_book,name='books.edit')
    
]