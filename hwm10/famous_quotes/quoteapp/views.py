from django.shortcuts import render, redirect

from .models import Quote, Tag, Author
from .forms import TagForm, QuoteForm

menu = ["About us", "Add quote", "Contacts", "Login"]

# # Create your views here.
# class QuoteHome(DataMixin, ListView):
#     model = Quote


def main(request):
    quotes = Quote.objects.all()
    for quote in quotes:
        print(quote.tag)
    return render(
        request,
        "quoteapp/index.html",
        {"quotes": quotes, "menu": menu, "title": "Main page"},
    )


def about(request):
    return render(request, "quoteapp/about.html", {"menu": menu, "title": "About us"})


def tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quoteapp:home")
        else:
            return render(request, "quoteapp/tag.html", {"form": form})

    return render(request, "quoteapp/tag.html", {"form": TagForm()})


def addquote(request):
    tags = Tag.objects.all()
    author = Author.objects.all()

    if request.method == "POST":
        form = QuoteForm(request.POST)
        print(request.POST["tags"])
        print(Tag.objects.filter(name__in=request.POST.getlist("tags")))
        # print(Author.objects.filter(name__in=request.POST.get("author")))
        if form.is_valid():
            new_note = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist("tags"))

            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            return redirect(to="quoteapp:home")
        else:
            return render(
                request,
                "quoteapp/addquote.html",
                {"tags": tags, "author": author, "form": form},
            )

    return render(
        request,
        "quoteapp/addquote.html",
        {"author": author, "tags": tags, "form": QuoteForm()},
    )
