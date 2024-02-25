from django import forms
from .models import Comment
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'email', 'text']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control w-50 border border-1 border-black m-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control w-50 border border-1 border-black m-2'}),
            
        }
