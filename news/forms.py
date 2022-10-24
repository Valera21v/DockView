from django import forms
from .models import News, Category


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),

        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
        }


class NewsUpdateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }
