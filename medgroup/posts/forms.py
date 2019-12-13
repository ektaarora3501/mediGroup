from django import forms
from .models import Post
from group.models import Register

class PostsCreateForm(forms.Form):
    title       = forms.CharField(required=True)
    author      = Register.username
    content     = forms.Textarea()

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title == "Dead" or title == "Death":
            raise forms.ValidationError('not a valid title')
        return title
