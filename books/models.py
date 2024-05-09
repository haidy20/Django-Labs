from django.db import models
from django.shortcuts import reverse, get_object_or_404
from categories.models import Category

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    nums = models.IntegerField(blank=True)
    author = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='bookstore/images',null=True,blank=True)
    code = models.CharField(max_length=100,unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category =models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="allbooks")


    def __str__(self):
        return f'{self.name}'
    

    @property
    def show_url(self):
     return reverse('books.show', args=[self.id])
    

    @property
    def delete_url(self):
     return reverse('books.delete', args=[self.id])
    

    @property
    def image_url(self):
       return f"/media/{self.image}"
    
    @classmethod
    def get_books_by_id(cls, id):
       return get_object_or_404(cls, pk=id)
    

    @property
    def edit_url(self):
       return reverse('books.edit', args=[self.id])
    

