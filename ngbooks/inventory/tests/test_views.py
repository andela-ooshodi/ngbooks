"""
Test inventory views here
"""

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from inventory.models import Category, Book

# Create your tests here.


class InventoryViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='Space',
            description='All about space'
        )
        self.book = Book.objects.create(
            name='Space Voyage',
            description='The journey of captain rogers',
            book_author='Captain Rogers',
            book_cat=self.category
        )

    def tearDown(self):
        Category.objects.all().delete()
        Book.objects.all().delete()

    def test_can_reach_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'inventory/base.html')

    def test_can_reach_404_page(self):
        response = self.client.get(reverse('404'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'inventory/404.html')

    def test_can_search_by_category(self):
        query_data = {
            'radio-opt': 'category',
            'name': 'space'
        }
        response = self.client.get(reverse('result'), query_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Space', response.content)
        self.assertIn('All about space', response.content)

    def test_can_search_by_book_title(self):
        query_data = {
            'radio-opt': 'book',
            'name': 'Space Voyage'
        }
        response = self.client.get(reverse('result'), query_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Space Voyage', response.content)
        self.assertIn('Captain Rogers', response.content)

    def test_can_search_by_partial_book_title(self):
        query_data = {
            'radio-opt': 'book',
            'name': 'voyage'
        }
        response = self.client.get(reverse('result'), query_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Space Voyage', response.content)
        self.assertIn('Captain Rogers', response.content)

    def test_cannot_find_category(self):
        query_data = {
            'radio-opt': 'category',
            'name': 'Not found'
        }
        response = self.client.get(reverse('result'), query_data)
        # redirect to 404 page
        self.assertEqual(response.status_code, 302)

    def test_cannot_find_book(self):
        query_data = {
            'radio-opt': 'book',
            'name': 'Not found'
        }
        response = self.client.get(reverse('result'), query_data)
        # redirect to 404 page
        self.assertEqual(response.status_code, 302)

    def test_empty_query(self):
        # Navigating to the result page without any query parameters
        response = self.client.get(reverse('result'))
        # redirect to 404 page
        self.assertEqual(response.status_code, 302)
