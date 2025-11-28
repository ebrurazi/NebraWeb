from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','started_on','finished_on','rating','notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        