from django.urls import path
from blog import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="blog-home"),
    path('post/create/', views.CreatePostView.as_view(), name="create-post"),
    path('post/detail/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name="post-update"),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name="delete-post"),
    path('author/<str:author>/', views.AuthorPostListView.as_view(), name="author"),
   
]