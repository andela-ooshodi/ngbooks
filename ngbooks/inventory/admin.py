from django.contrib import admin

# Register your models here.
from .models import Category, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [BookInline]


admin.site.register(Category, CategoryAdmin)
