from django import forms
from categories.models import Category

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if not name:
          raise forms.ValidationError("Please enter a name.")
        if not description:
          raise forms.ValidationError("Please enter a description.")

        return cleaned_data
