from categories.views import landing
from django.urls import path
from categories.views import home, create_category, categories_index,category_show
# ,show_category_details

# include categories urls
urlpatterns = [
 path('categories',landing,name='categories'),
 path('home',home,name='categories.home'),
 path('create',create_category,name='category'),
 path('',categories_index,name='categories.index'),
#  path('categories/<int:pk>/', show_category_details, name='categories.show'),
 path('<int:id>', category_show, name='categories.show')


]
