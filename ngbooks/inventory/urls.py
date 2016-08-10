"""
URL config for accessing views of the inventory app
"""

from django.conf.urls import url
from inventory.views import IndexView, ResultView, NotFoundView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^result/?$', ResultView.as_view(), name='result'),
    url(r'^404/?$', NotFoundView.as_view(), name='404'),
]
