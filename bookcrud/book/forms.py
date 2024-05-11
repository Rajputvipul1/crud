from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Specifies the model associated with this form
        fields = ['title', 'author', 'publication_date', 'cover_image']  # Specifies the fields to include in the form

        # Specifies custom widgets for each form field to control their appearance
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # TextInput for the title field with the 'form-control' class
            'author': forms.TextInput(attrs={'class': 'form-control'}),  # TextInput for the author field with the 'form-control' class
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # DateInput for the publication_date field with the 'form-control' class and type 'date'
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),  # FileInput for the cover_image field with the 'form-control' class
        }
