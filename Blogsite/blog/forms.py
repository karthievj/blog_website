from django import forms
from .models import BlogPost , Profile

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','slug','content')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Blog'}),
            'slug' : forms.TextInput(attrs={'class':'form-control','placeholder':'Copy the title with no space and hyphen inbetweeen '}),
            'content' : forms.Textarea(attrs={'class':'form-control','placeholder':'Content of the Blog'})
        }