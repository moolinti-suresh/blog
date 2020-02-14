from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('post/create/', views.create_post, name="create-post"),
    path('post/<int:id>/', views.post_details, name="post-detail"),
    path('author/<str:author>/', views.author_posts, name="author"),
]