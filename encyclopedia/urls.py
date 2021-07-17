from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("NewPage/", views.NewPage, name="NewPage"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("search/", views.search, name="search")
 

]
