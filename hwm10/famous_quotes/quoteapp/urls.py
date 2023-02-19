from django.urls import path
from . import views

app_name = "quoteapp"

urlpatterns = [
    path("", views.QuoteHome.as_view(), name="home"),
    path("tag/", views.AddTag.as_view(), name="tag"),
    path("addquote/", views.addquote, name="addquote"),
    path("addauthor/", views.addauthor, name="addauthor"),
    path("post/<int:post_id>", views.ShowPost.as_view(), name="post"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logoutuser, name="logout"),
]
