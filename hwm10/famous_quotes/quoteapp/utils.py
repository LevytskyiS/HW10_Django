from .models import *

menu = [
    {"title": "Main page", "url_name": "quoteapp:home"},
    {"title": "Add quote", "url_name": "quoteapp:addquote"},
    {"title": "Add author", "url_name": "quoteapp:addauthor"},
    {"title": "Add tag", "url_name": "quoteapp:tag"},
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu = menu[:1]

        context["menu"] = user_menu
        return context
