from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/home.html', context={
            'page_obj': page_obj
        })

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post.html', context={
        'post': post
    })

def contact(request):
    return render(request, 'blog/contact.html')

def thanks(request):
    return render(request, 'blog/thanks.html')

def signup(request):
    return render(request, 'blog/signup.html')

def signin(request):
    return render(request, 'blog/signin.html')

def search(request):
    return render(request, 'blog/search.html')