from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from recipes.forms import RatingForm

from django.contrib.auth.mixins import LoginRequiredMixin

from recipes.models import Recipe


class RecipeListView(ListView):
    model = Recipe
    context_object_name = "recipe_list"
    template_name = "recipes/list.html"
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query:
            query = ""
        return Recipe.objects.filter(description__icontains=query)


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = "recipe"
    template_name = "recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ["name", "author", "description", "image"]
    template_name = "recipes/new.html"
    success_url = "/"


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ["name", "author", "description", "image"]
    template_name = "recipes/edit.html"
    success_url = "/"


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = "/"


def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            try:
                rating = form.save(commit=False)
                rating.recipe = Recipe.objects.get(pk=recipe_id)
                rating.save()
            except Recipe.DoesNotExist:
                return redirect("recipes_list")
    return redirect("recipe_detail", pk=recipe_id)
