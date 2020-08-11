from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name="home" ),
path('certificate',views.certificateView.as_view() ,name="certificate"),
path('blog',views.blog,name="blog"),
path('post/<slug:slug>',views.post_detail,name="post_detail"),
path('catagory/<int:pk>',views.blog_by_catagory,name="blog_by_catagory"),

]
