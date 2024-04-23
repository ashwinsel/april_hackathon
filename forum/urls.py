from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('categories/<int:category_id>/create_thread/', views.create_thread, name='create_thread'),
    path('categories/<int:category_id>/threads/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('categories/<int:category_id>/threads/<int:thread_id>/create_post/', views.create_post, name='create_post'),
    path('posts/<int:post_id>/like/', views.like_post, name='like_post'),
]

