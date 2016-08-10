"""
View logic
"""

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, View
from .models import Category, Book


class IndexView(TemplateView):
    # Base view
    template_name = 'inventory/base.html'


class ResultView(View):
    # Result view
    # Function that handles the get request received in this view
    def get(self, request):
        # get the option the user wants to search by
        search_option = request.GET.get('radio-opt')
        if search_option == 'category':
            # query for books by category
            category_name = request.GET.get('name')
            try:
                category = Category.objects.get(name__iexact=category_name)

                # get context
                context = {'category': category}
                return render(request, 'inventory/result.html', context)
            except Category.DoesNotExist:
                return redirect(reverse('404'))

        elif search_option == 'book':
            # query for books by book title
            book_name = request.GET.get('name')

            book = Book.objects.filter(name__icontains=book_name)

            if not book:
                return redirect(reverse('404'))

            # get context
            context = {'books': book}
            return render(request, 'inventory/result.html', context)

        else:
            return redirect(reverse('404'))


class NotFoundView(TemplateView):
    # 404 view
    template_name = 'inventory/404.html'
