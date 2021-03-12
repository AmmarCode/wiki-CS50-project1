from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>/", views.entry, name="entry"),
    path("new", views.new, name="new"),
    path("save", views.save, name="save"),
    path("edit", views.edit, name="edit"),
    path("save_edit", views.save_edit, name="save_edit"),
    path("search", views.search, name="search"),
    path("random", views.random_entry, name="random")
]
