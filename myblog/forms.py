from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','preview', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tag(s)'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder':'Author'}),
            'preview': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Preview of post'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Content'}),
        }