from django import forms 
from . models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput())
    content = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Post
        fields = ['title', 'content']