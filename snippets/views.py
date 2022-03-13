from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet, Category
from .forms import SnippetForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect("index")
    return render(request, "home.html")


@login_required
def index(request):
    snippets = Snippet.objects.all()
    categories = Category.objects.all()
    return render(request, "index.html", {"snippets": snippets, "categories": categories})


@login_required
def detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    form = SnippetForm()
    return render(request, "detail.html", {"snippet": snippet, "pk": pk, "form": form})


def add(request):
    if request.method =='GET':
        form = SnippetForm()
    else:
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='index')
    return render(request, "add.html", {"form": form})


def edit(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'GET':
        form = SnippetForm(instance=snippet)
    else:
        form = SnippetForm(data=request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect(to="index")
    return render(request, "edit.html", {"snippet": snippet, "form": form, "pk": pk})


def delete(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        snippet.delete()
        return redirect(to='index')
    return render(request, "delete.html", {"snippet": snippet, "pk": pk})


def title(request):
    title = Snippet.objects.order_by('title')
    categories = Category.objects.all()
    context = {'Snippets': title, 'categories': categories}
    return render(request, 'index.html', context)


@login_required
def oldest(request):
    oldest = Snippet.objects.order_by('created_at')
    categories = Category.objects.all()
    context = {'snippets': oldest, 'categories': categories}
    return render(request, 'index.html', context)


@login_required
def newest(request):
    newest = Snippet.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {'snippets': newest, 'categories': categories}
    return render(request, 'index.html', context)

# @login_required
# def add_favorite(request, snippet_pk):
#     snippet = get_object_or_404(Snippet, pk=snippet_pk)
#     user = request.user
#     user.favorite_snippets.add(snippet)
#     return redirect("snippet_detail", pk=snippet.pk)

# @login_required
# def delete_favorite(request, snippet_pk):
#     snippet = get_object_or_404(Snippet, pk=snippet_pk)
#     request.user.favorite_snippets.remove(snippet)
#     return redirect("snippet_detail", pk=snippet.pk)

@login_required
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    snippets = category.snippets.all()
    return render(request, "category.html", {"category": category, "snippets": snippets})