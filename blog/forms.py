from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField()
    hashtags = forms.CharField()

class CreateComment(forms.Form):
    comment = forms.CharField(max_length=200)
