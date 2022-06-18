from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from .forms import SignUpForm, SignInForm, FeedBackForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from taggit.models import Tag

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'blog/signup.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'blog/signup.html', context={
            'form': form
        })

class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'blog/signin.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'blog/signin.html', context={
            'form': form
        })

class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'blog/contact.html', context={
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'От {name} | {subject}', message, from_email, ['jam.d456@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('thanks')
        return render(request, 'blog/contact.html', context={
            'form': form
        })

class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ""
        if query:
            results = Post.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        paginator = Paginator(results, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/search.html', context={
            'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        })

class TagView(View):
    def get(self, request, name, *args, **kwargs):
        tag = get_object_or_404(Tag, name=name)
        posts = Post.objects.filter(tag=tag)
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        common_tags = Post.tag.most_common()
        return render(request, 'blog/tag.html', context={
            'title': f'#ТЕГ {tag}',
            'page_obj': page_obj,
            'common_tags': common_tags
        })

def home(request):
    posts = Post.objects.order_by('-created_at')
    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/home.html', context={
            'page_obj': page_obj
        })

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    common_tags = Post.tag.most_common()
    last_posts = Post.objects.all().order_by('-id')[:3]
    return render(request, 'blog/post.html', context={
        'post': post,
        'common_tags': common_tags,
        'last_posts': last_posts
    })


def thanks(request):
    return render(request, 'blog/thanks.html')
