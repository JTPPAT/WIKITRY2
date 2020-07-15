from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("newpage", views.newpage, name="newpage"),
    path("random_page", views.random_page, name= "random_page"),
    path("wiki/<str:title>/edit", views.editpage2, name="editpage2"),
    path("edit1/<str:title>", views.editpage1, name="editpage1"),
    path("search", views.search, name="search"),
]