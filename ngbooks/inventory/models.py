"""
Model for inventory app
"""

from django.db import models

# Create your models here.


class Base(models.Model):
    # Base class for the inventory app models
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True, default='No description')

    class Meta:
        abstract = True

    # returns a string representation of the object
    def __str__(self):
        return self.name


class Category(Base):
    pass


class Book(Base):
    book_author = models.CharField(max_length=200, default='Unknown')
    book_cat = models.ForeignKey(Category, related_name='book')
