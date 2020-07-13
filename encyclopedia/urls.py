from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("newpage", views.newpage, name="newpage"),
    path("random_page", views.random_page, name= "random_page"),
    path("error", views.error, name="error"),
]