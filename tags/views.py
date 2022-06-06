from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


try:
    from tags.models import Tag
except Exception:
    Tag = None


# Create your views here.


class TagListView(ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "tags/list.html"
    paginate_by = 15


class TagDetailView(DetailView):
    model = Tag
    context_object_name = "tags"
    template_name = "tags/detail.html"


class TagCreateView(CreateView):
    model = Tag
    template_name = "tags/create.html"
    success_url = "/"


class TagUpdateView(UpdateView):
    model = Tag
    template_name = "tags/update.html"
    success_url = "/"


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tags/delete.html"
    success_url = "/"
