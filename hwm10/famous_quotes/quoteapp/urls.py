from django.urls import path
from . import views

app_name = "quoteapp"

urlpatterns = [
    path("", views.main, name="home"),
    path("about/", views.about, name="about"),
    path("tag/", views.tag, name="tag"),
    path("addquote/", views.addquote, name="addquote"),
]
