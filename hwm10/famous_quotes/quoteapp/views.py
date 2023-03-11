from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


from .models import Quote, Tag, Author
from .forms import TagForm, QuoteForm, AuthorForm, RegisterUserForm, LoginUserForm
from .utils import DataMixin


class QuoteHome(DataMixin, ListView):
    model = Quote
    template_name = "quoteapp/index.html"
    context_object_name = "quotes"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Quotes to Scrape")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AddTag(LoginRequiredMixin, DataMixin, CreateView):
    form_class = TagForm
    template_name = "quoteapp/tag.html"
    # login_url = reverse_lazy("quoteapp:home") - альтернатива get_success_url
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add tag")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_success_url(self):
        return reverse("quoteapp:home")

    # Вместо дублирования этой функции в разных классах можно указать
    # LOGIN_REDIRECT_URL = "/" в settings.py


def addquote(request):

    author = Author.objects.all()
    tags = Tag.objects.all()

    if request.method == "POST":
        form = QuoteForm(request.POST)

        if form.is_valid():
            try:
                new_quote = form.save()
                choice_tags = Tag.objects.filter(name__in=request.POST.getlist("tags"))

                for tag in choice_tags.iterator():
                    new_quote.tag.add(tag)
                return redirect(to="quoteapp:home")
            except:
                form.add_error(None, "Quote saving error")

        else:
            return render(
                request,
                "quoteapp/addquote.html",
                {"form": form, "author": author, "tags": tags},
            )

    return render(
        request,
        "quoteapp/addquote.html",
        {"form": QuoteForm(), "author": author, "tags": tags},
    )


def addauthor(request):

    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect(to="quoteapp:home")
            except:
                form.add_error(None, "Quote saving error")

        else:
            return render(
                request,
                "quoteapp/addquote.html",
                {"form": form},
            )

    return render(
        request,
        "quoteapp/addauthor.html",
        {"form": AuthorForm()},
    )


class ShowPost(DataMixin, DetailView):
    model = Author
    template_name = "quoteapp/post.html"
    pk_url_kwarg = "post_id"
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Post")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "quoteapp/register.html"
    success_url = reverse_lazy("quoteapp:login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("quoteapp:home")


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "quoteapp/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Log in")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


def logoutuser(request):
    logout(request)
    return redirect(to="quoteapp:home")


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "quoteapp/password_reset.html"
    email_template_name = "quoteapp/password_reset_email.html"
    html_email_template_name = "quoteapp/password_reset_email.html"
    success_url = reverse_lazy("quoteapp:password_reset_done")
    success_message = (
        "An email with instructions to reset your password has been sent to %(email)s."
    )
    subject_template_name = "quoteapp/password_reset_subject.txt"
