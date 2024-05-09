"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello', hello, name='hellopage'),
    # path('wlcm',welcome,name='welcomepage'),
    # path('land',landing,name='books'),
    # # specify part of the URL --> variable and must be int
    # path('bok/<int:id>',book_details,name='bok.datails'),
    # path('books',book_landing,name='categories')
    # include categories urls file in the main url
    path('categories/', include('categories.urls')),
    # include boooks urls
    path('books/',include("books.urls")),
    # path('bookstore/', admin.site.urls),
    # path('bookstore/', include('pages.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
