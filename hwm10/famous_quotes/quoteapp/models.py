from django.db import models
from django.urls import reverse


class Quote(models.Model):
    quote = models.CharField(max_length=255)
    author = models.ForeignKey("Author", on_delete=models.PROTECT)
    tag = models.ManyToManyField("Tag")
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.quote}"


class Author(models.Model):
    fullname = models.CharField(max_length=255, unique=True)
    born_date = models.CharField(max_length=20)
    born_location = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.fullname}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"
