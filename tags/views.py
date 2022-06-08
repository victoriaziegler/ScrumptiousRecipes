from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


from tags.models import Tag


# Create your views here.


class TagListView(ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "tags/list.html"
    paginate_by = 5


class TagDetailView(DetailView):
    model = Tag
    context_object_name = "tags"
    template_name = "tags/detail.html"


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "tags/new.html"
    fields = ["name"]
    success_url = "/"


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = "tags/edit.html"
    fields = ["name"]
    success_url = "/"


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = "tags/delete.html"
    success_url = "/"
