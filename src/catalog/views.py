from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from .models import Book, Author
from .forms import BookForm, AuthorForm, SearchForm


def homepage(request):
    return render(request, "homepage.html")


def show_books(request):
    books_list = Book.objects.all()
    search_form = SearchForm()
    return render(request, "show_books.html", {"books": books_list, "form": search_form})


def add_book(request):
    form = BookForm()
    if request.method == "GET":
        return render(request, "add_book.html", {"form": form})

    form = BookForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse("catalog:show-books"))
    else:
        return render(request, "add_book.html", {"form": form})


def show_authors(request):
    authors_list = Author.objects.all()
    return render(request, "show_authors.html", {"authors": authors_list})


def add_author(request):
    form = AuthorForm()
    if request.method == "GET":
        return render(request, "add_author.html", {"form": form})

    form = AuthorForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse("catalog:show-authors"))
    else:
        return render(request, "add_author.html", {"form": form})


def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(instance=book)
    if request.method == "GET":
        return render(request, "edit_book.html", {"form": form, "book_id": book_id})

    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse("catalog:show-books"))
    else:
        return render(request, "edit_book.html", {"form": form, "book_id": book_id})


def edit_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    form = AuthorForm(instance=author)
    if request.method == "GET":
        return render(request, "edit_author.html", {"form": form, "author_id": author_id})

    form = AuthorForm(request.POST, instance=author)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse("catalog:show-authors"))
    else:
        return render(request, "edit_author.html", {"form": form, "author_id": author_id})


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return HttpResponseRedirect(reverse("catalog:show-books"))


def delete_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    author.delete()
    return HttpResponseRedirect(reverse("catalog:show-authors"))

# @require_POST
# def filter_books(request):
#     books = Book.objects.all()
#     search_text = request.POST.get("search_text")
#     published_date_min = request.POST.get("published_date_min")
#     published_date_max = request.POST.get("published_date_max")
#     price_min = request.POST.get("price_min")
#     price_max = request.POST.get("price_max")

#     if search_text:
#         books = books.filter(name__icontains=search_text) | books.filter(
#             author__name__icontains=search_text)
#     if published_date_min:
#         books = books.filter(published_date__gte=published_date_min)
#     if published_date_max:
#         books = books.filter(published_date__lte=published_date_max)
#     if price_min:
#         books = books.filter(price__gte=price_min)
#     if price_max:
#         books = books.filter(price__lte=price_max)
#     return render(request, "show_books.html", {"books": books, "search_text": search_text, "published_date_min": published_date_min, "published_date_max": published_date_max, "price_min": price_min, "price_max": price_max})


def filter_books(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        search_text = form.cleaned_data.get("search_text")
        published_date_min = form.cleaned_data.get("published_date_min")
        published_date_max = form.cleaned_data.get("published_date_max")
        price_min = form.cleaned_data.get("price_min")
        price_max = form.cleaned_data.get("price_max")

        books = Book.objects.all()

        print(search_text, published_date_min,
              published_date_max, price_min, price_max)

        if search_text:
            books = books.filter(name__icontains=search_text) | books.filter(
                author__name__icontains=search_text)
        if published_date_min:
            books = books.filter(published_at__gte=published_date_min)
        if published_date_max:
            books = books.filter(published_at__lte=published_date_max)
        if price_min:
            books = books.filter(price__gte=price_min)
        if price_max:
            books = books.filter(price__lte=price_max)

        print(books)
        return render(request, "show_books.html", {"books": books, "form": form})
    else:
        return render(request, "show_books.html", {"form": form})
