from django import forms

from .models import Author, Book


class DateInput(forms.DateInput):
    input_type = "date"


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            'published_at': DateInput(),
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class SearchForm(forms.Form):
    search_text = forms.CharField(
        max_length=100, required=False, label="Search", widget=forms.TextInput(attrs={"placeholder": "Book Name or Author Name"}))
    published_date_min = forms.DateField(
        required=False, widget=DateInput(), label="Published Date From")
    published_date_max = forms.DateField(
        required=False, widget=DateInput(), label="Published Date To")
    price_min = forms.DecimalField(required=False, label="Price From", widget=forms.NumberInput(
        attrs={"placeholder": "Price From"}))
    price_max = forms.DecimalField(required=False, label="Price To", widget=forms.NumberInput(
        attrs={"placeholder": "Price To"}))
