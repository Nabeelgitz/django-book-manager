# Create your models here.

# website/models.py

from django.db import models

class BookDetail(models.Model):
    book_id = models.AutoField(primary_key=True)   # Auto increment by default
    name = models.CharField(max_length=200)       # Book name
    author = models.CharField(max_length=200)     # Author name
    category = models.CharField(max_length=100, default="None")  # Default None
    date = models.DateField()                     # Publish/added date

    def __str__(self):
        return f"{self.name} by {self.author}"

