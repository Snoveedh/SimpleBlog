from django import forms
from django.forms import widgets
from .models import Comment, Post , Category, Comment

#choices = [('coding', 'coding'), ('News', 'News'), ('Entertainment', 'Entertainment'), ('cricket', 'cricket')]

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body','snippet', 'header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'},),
            # 'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':choices}), # To checl the choice set is working or not
            # 'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'This placeholder for the title'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value':'','id' : 'elder', 'type':'hidden'}),
            # 'author' : forms.Select(attrs={'class': 'form-control'}),
            # 'category' : forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body','snippet') # removed "author"

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'},),
            # 'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'This placeholder for the title'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'author' : forms.Select(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
        }




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body') # removed "author"

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'},),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }