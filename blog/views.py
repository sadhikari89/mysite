from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    template = "home.html"
    context = {}
    return render (request, template, context)

def post_list(request):
    posts = Post.published.all()
    return render (request, 'blog/post/list.html',
                   {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request, 'blog/post/list.html',
                   {'post': post})