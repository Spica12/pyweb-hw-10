from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Quote, Author


# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    return render(request, 'quoteapp/index.html', {'quotes': quotes})


def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})


def quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            author = Author.objects.filter(id=request.POST['author']).first()
            new_quote.author = author

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quoteapp:main')
        else:

            return render(request, 'quoteapp/quote.html', {"authors": authors, 'tags': tags,'form': form})

    return render(request, 'quoteapp/quote.html', {"authors": authors, 'tags': tags, 'form': QuoteForm()})


def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/author.html', {'form': form})

    return render(request, 'quoteapp/author.html', {'form': AuthorForm()})


def detail(request, author_fullanme):
    author = get_object_or_404(Author, fullname=author_fullanme)

    return render(request, "quoteapp/detail.html", {"author": author})


def delete_all_quotes(request):
    quotes = Quote.objects.all()
    for quote in quotes:
        quote.delete()

    return redirect(to='quoteapp:main')


def delete_all_authors(request):
    authors = Author.objects.all()
    for author in authors:
        author.delete()

    return redirect(to='quoteapp:main')


def delete_all_tags(request):
    tags = Tag.objects.all()
    for tag in tags:
        tag.delete()

    return redirect(to='quoteapp:main')
