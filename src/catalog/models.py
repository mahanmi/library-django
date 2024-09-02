from django.db import models
from datetime import date

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    email = models.EmailField("Email", unique=True)
    created_at = models.DateTimeField("Created time", auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField("Book Name", max_length=255, db_index=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, verbose_name="Author")
    price = models.BigIntegerField("Price")
    quantity = models.IntegerField("Quantity of available books")
    published_at = models.DateField("Date of book publish", default=date.today)
    updated_at = models.DateTimeField("Last time Modified", auto_now=True)
    created_at = models.DateTimeField("Created time", auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.author}"

    def details(self) -> str:
        return f"price : {self.price}, published at : {self.published_at}, quantity : {self.quantity}"
