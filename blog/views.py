from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def post(request):
    return render(request, 'blog/post.html')

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