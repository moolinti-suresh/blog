from django.shortcuts import render, redirect
from . models import Post
from . forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page',1)
    page = paginator.page(page_num)
    return render(request, 'blog/home.html', {'page_obj':page})

@login_required
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = form = PostForm(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            form.save()
            messages.success(request, "Your post has been created!")
            return redirect('post-detail', id=newpost.id)
    return render(request, 'blog/create-post.html', {'form':form})


def post_details(request, id=None):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post-details.html', {'post':post})

def author_posts(request, author=None):
    posts = Post.objects.filter(author__username__startswith = author).order_by('-date_posted')
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page',1)
    page = paginator.page(page_num)
    context = {
        'page_obj':page, 
        'posts': paginator.count,
        'username': author,
    }
    return render(request, 'blog/author-posts.html', context)
