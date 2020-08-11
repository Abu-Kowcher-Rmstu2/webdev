from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.detail, name='detail'),
    path("add/",views.add,name="add"),
    path('search',views.search,name='search'),
    path('search_result',views.search,name="search_result"),
    path('edit/<str:title>',views.edit ,name="edit"),
    path('save_edit/<str:title>',views.save_edit,name="save_edit"),
    path('random/',views.random_call,name='random_call'),
]
