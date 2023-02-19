from django.forms import (
    ModelForm,
    CharField,
    EmailField,
    EmailInput,
    TextInput,
    PasswordInput,
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


from .models import Tag, Quote, Author


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ["name"]


class QuoteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["author"].empty_label = "Chose an author"

    class Meta:
        model = Quote
        fields = ["quote", "author", "tag"]
        widgets = {
            "quote": TextInput(attrs={"cols": 60, "rows": 10}),
        }


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]


class RegisterUserForm(UserCreationForm):

    username = CharField(label="Login", widget=TextInput(attrs={"class": "form-input"}))
    email = EmailField(label="Email", widget=EmailInput(attrs={"class": "form-input"}))
    password1 = CharField(
        label="Password", widget=PasswordInput(attrs={"class": "form-input"})
    )
    password2 = CharField(
        label="Password confirmation",
        widget=PasswordInput(attrs={"class": "form-input"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = CharField(label="Login", widget=TextInput(attrs={"class": "form-input"}))
    password = CharField(
        label="Password", widget=PasswordInput(attrs={"class": "form-input"})
    )
