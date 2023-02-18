from django.db.models import Count

from .models import *

menu = [
    {"title": "Quotes to Scrape", "url_name": "home"},
    {"title": "Add quote", "url_name": "add_quote"},
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
