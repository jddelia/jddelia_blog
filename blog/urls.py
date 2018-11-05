from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='blog-index'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('projects/', views.projects, name='blog-projects'),
    path('posts/<int:post_id>/', views.post, name='blog-post')
]
