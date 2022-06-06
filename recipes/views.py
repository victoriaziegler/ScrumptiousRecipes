from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    context_object_name = "recipe_list"
    template_name = "recipes/list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = "recipe"
    template_name = "recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()
        return context


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = "/"


def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.recipe = Recipe.objects.get(pk=recipe_id)
            rating.save()
    return redirect("recipe_detail", pk=recipe_id)
