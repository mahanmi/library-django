from django.urls import path

from . import views

app_name = "catalog"
urlpatterns = [
    path("", views.homepage, name="home"),
    path("list/", views.show_books, name="show-books"),
    path("show_authors/", views.show_authors, name="show-authors"),
    path("add_book/", views.add_book, name="add-book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit-book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete-book"),
    path("add_author/", views.add_author, name="add-author"),
    path("edit_author/<int:author_id>/", views.edit_author, name="edit-author"),
    path("delete_author/<int:author_id>/",
         views.delete_author, name="delete-author"),
    path("filter_books/", views.filter_books, name="filter-books"),
]
