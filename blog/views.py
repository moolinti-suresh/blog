from django.shortcuts import render, redirect, get_object_or_404
from . models import Post
from . forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class HomeView(ListView):
    template_name = 'blog/home.html'
    model = Post        #<queryset = Post.objects.all() or def get_query_set(self)>
    context_object_name = 'posts'
    paginate_by = 3


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create-post.html'
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return  super().form_valid(form)


class PostDetailView(DetailView):
    template_name = 'blog/post-details.html'
    model = Post
    
class AuthorPostListView(ListView):
    template_name = 'blog/author-posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        author = get_object_or_404(User, username=self.kwargs.get('author'))
        posts = Post.objects.filter(author__username__startswith = author).order_by('-date_posted')
        return posts

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        author = get_object_or_404(User, username=self.kwargs.get('author'))
        posts = Post.objects.filter(author__username__startswith = author).order_by('-date_posted')
        context['username'] = author
        context['posts_count'] = posts.count
        return context

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'blog/post-delete.html'
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'blog/create-post.html'
    model = Post
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object() #getting the current object
        if self.request.user == post.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)