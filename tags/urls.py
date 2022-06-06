from django.urls import path

from tags.views import (
    TagCreateView,
    TagDeleteView,
    TagDetailView,
    TagListView,
    TagUpdateView,
)

urlpatterns = [
    path("", TagListView.as_view(), name="tags_list"),
    path("<int:pk>/", TagDetailView.as_view(), name="tags_detail"),
    path("<int:pk>/delete/", TagDeleteView.as_view(), name="tags_delete"),
    path("new/", TagCreateView.as_view(), name="tags_new"),
    path("<int:pk>/edit/", TagUpdateView.as_view(), name="tags_edit"),
]
