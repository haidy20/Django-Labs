from django import forms
from books.models import Book
# from django.db import IntegrityError


class BookForm(forms.Form):
    name = forms.CharField(max_length=100, label='Book Name', required=True)
    price = forms.IntegerField(label='Price', required=True)
    nums = forms.IntegerField(label='Number of pages')
    author = forms.CharField(max_length=100, label='Author')
    image = forms.ImageField(required=False, label='Image')
    code = forms.CharField(max_length=100)

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise forms.ValidationError('Name length must be greater than 2')
        return name
    
    
class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError('Name length must be greater than 2')
        return cleaned_data



    # def clean_code(self):
    #     code = self.cleaned_data['code']
    #     code_found = Book.objects.filter(code=code).exists()
    #     if code_found and self.instance:
    #         raise forms.ValidationError('Code is used before ,pls choose another one')
    #     return code
    