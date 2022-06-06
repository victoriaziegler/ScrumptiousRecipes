from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from recipes.forms import RatingForm

try:
    from recipes.forms import RecipeForm
    from recipes.models import Recipe
except Exception:
    RecipeForm = None
    Recipe = None


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["name", "author", "description", "image"]
    template_name = "recipes/new.html"
    success_url = "/"


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ["name", "author", "description", "image"]
    template_name = "recipes/edit.html"
    success_url = "/"


class RecipeListView(ListView):
    model = Recipe
    context_object_name = "recipes"
    template_name = "recipes/list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = "recipe"
    template_name = "recipes/detail.html"


def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.recipe = Recipe.objects.get(pk=recipe_id)
            rating.save()
    return redirect("recipe_detail", pk=recipe_id)
