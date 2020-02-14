from django.urls import path
from blog import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="blog-home"),
    path('post/create/', views.CreatePostView.as_view(), name="create-post"),
    path('post/delete/<int:id>/', views.PostDeleteView.as_view(), name="delete-post"),
    path('post/<int:id>/', views.PostDetailView.as_view(), name="post-detail"),
    path('author/<str:author>/', views.AuthorPostListView.as_view(), name="author"),
   
]