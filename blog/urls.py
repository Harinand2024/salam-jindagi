from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    # Blog list
    path('blogs/', views.blog_list, name='blog_list'),

    # Blog detail
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),

    # Category wise blogs
    path('category/<slug:slug>/', views.category_blogs, name='category_blogs'),

    # Tag wise blogs
    path('tag/<slug:slug>/', views.tag_blogs, name='tag_blogs'),
]
