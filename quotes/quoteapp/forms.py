from django.forms import ModelForm, CharField, DateField, TextInput, DateInput
from .models import Tag, Quote, Author


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class QuoteForm(ModelForm):

    quote = CharField(min_length=10, max_length=150, required=True, widget=TextInput())
    author = CharField(min_length=5, max_length=50, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']


class AuthorForm(ModelForm):

    fullname = CharField(min_length=10, max_length=150, required=True, widget=TextInput())
    born_date = DateField(required=True, widget=DateInput(attrs={'type': 'date'}))
    born_location = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    description = CharField(min_length=5, max_length=50, required=True, widget=TextInput())


    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
