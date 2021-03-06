from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("NewPage/", views.NewPage, name="NewPage"),
    path("search/", views.search, name="search"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("wiki/edit/<str:title>", views.edit, name="edit"),
    path("NewPage/edit/<str:title>", views.edit, name="edit"),
    path("wiki/save/", views.save, name="save"),
    path("random/", views.randomPage, name="randomPage")
 

]
