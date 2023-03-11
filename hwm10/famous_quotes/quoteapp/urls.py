from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
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
    path("reset-password/", views.ResetPasswordView.as_view(), name="password_reset"),
    path(
        "reset-password/done/",
        PasswordResetDoneView.as_view(
            template_name="quoteapp/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset-password/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="quoteapp/password_reset_confirm.html",
            success_url="/quoteapp/reset-password/complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "quoteapp/reset-password/complete/",
        PasswordResetCompleteView.as_view(
            template_name="quoteapp/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
